import asyncio
from http import HTTPStatus
from os import listdir, path
from unittest.mock import patch
from xml.etree import ElementTree as ET

import pytest
from pytest_httpserver import HTTPServer
from werkzeug import Request, Response

from nast.aio import api
from nast.model import NationCategory, WAStatus, WAVote


NATION_SHARD_MAP = {
    "wa": "UNSTATUS",
}


def mock_api(request):
    if "nation" in request.args:
        dirname = path.join(path.dirname(__file__), "data/nations")
        return mock_api_response(request, request.args["nation"], dirname, NATION_SHARD_MAP)
    if "region" in request.args:
        dirname = path.join(path.dirname(__file__), "data/regions")
        return mock_api_response(request, request.query["region"], dirname)


def mock_api_response(request, name, dirname, shard_map):
    xml = find_xml(name, dirname)
    if xml is None:
        return Response(status=HTTPStatus.NOT_FOUND)
    if "q" not in request.args or request.args["q"] == "":
        return Response(response=xml, status=HTTPStatus.OK, mimetype="text/xml")
    shards = set(request.args["q"].split("+"))
    xml = ET.fromstring(xml)
    ret = ET.Element(xml.tag)
    for shard in shards:
        tag = shard_map.get(shard) or shard.upper()
        ret.append(xml.find(tag))
    return Response(response=ET.tostring(ret), status=HTTPStatus.OK, mimetype="text/xml")


def find_xml(name, dirname):
    for filename in listdir(dirname):
        if filename[:-4] == name:
            with open(path.join(dirname, filename), encoding="utf8") as file:
                return file.read()


@pytest.fixture(scope="module", autouse=True)
def http_server():
    server = HTTPServer(port=8080)
    server.expect_request("/api").respond_with_handler(mock_api)
    if not server.is_running():
        server.start()
    yield server
    if server.is_running():
        server.stop()


@patch("nast.aio.api.URL", "http://localhost:8080/api")
def test_nation_all_shards():
    nation = asyncio.run(api.nation("testlandia"))


@patch("nast.aio.api.URL", "http://localhost:8080/api")
@pytest.mark.parametrize(
    "shard,attr,expected",
    [
        ("name", "name", "Testlandia"),
        ("dbid", "dbid", 1),
        ("type", "type", "Hive Mind"),
        ("motto", "motto", "Fixed, thanks."),
        ("category", "category", NationCategory.INOFFENSIVE_CENTRIST_DEMOCRACY),
        ("wa", "wa_status", WAStatus.DELEGATE),
        ("endorsements", "endorsements", ["nationalist_gold_union", "international_silver_combine"]),
        ("gavote", "ga_vote", WAVote.UNDECIDED),
        ("scvote", "sc_vote", WAVote.UNDECIDED),
        ("region", "region", "Testregionia"),
        ("population", "population", 45032000000),
        ("tax", "tax", 87.7),
        ("animal", "animal", "★★★ nautilus ★★★"),
        ("animaltrait", "animal_trait", "frolics freely in the nation's sparkling oceans"),
        ("currency", "currency", "Kro-bro-ünze"),
    ]
)
def test_nation_shards(shard, attr, expected):
    nation = asyncio.run(api.nation("testlandia", shards=[shard]))
    assert getattr(nation, attr) == expected
