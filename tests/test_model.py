from os import path
from unittest.mock import patch

from nast.model import Nation, NationCategory, WAStatus


def test_nation_shards():
    filename = path.join(path.dirname(__file__), "data/nations/testlandia.xml")
    with open(filename) as file:
        xml = file.read()
    nation = Nation.from_xml(xml)

    assert nation.name == "Testlandia"
    assert nation.type == "Hive Mind"
    assert nation.motto == "Fixed, thanks."
    assert nation.category == NationCategory.INOFFENSIVE_CENTRIST_DEMOCRACY
    assert nation.wa_status == WAStatus.DELEGATE
