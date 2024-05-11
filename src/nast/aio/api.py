from aiohttp import ClientSession
from asyncio import Lock, sleep
from http import HTTPStatus
import logging as log
from time import time

from nast.model import Nation


URL = "https://www.nationstates.net/cgi-bin/api.cgi"
USER_AGENT ="Lieutenant Lou Lou/1.0 (by:gulliverpembroke@gmail.com; usedBy:Ysengrim)"
_limit = 1
_reset = time()
_lock = Lock()
_headers = {"User-Agent": USER_AGENT}


async def nation(name, shards=None, **kwargs):
    shards = shards or []
    return Nation.from_xml(await _request(nation=name, q="+".join(shards), **kwargs))


async def region(name, shards=None, **kwargs):
    shards = shards or []
    return await _request(region=name, q="+".join(shards), **kwargs)


async def _request(**params):
    global _limit, _reset

    async with _lock:
        now = time()
        if _limit <= 0 and now < _reset:
            await sleep(_reset - now)

    async with ClientSession() as session:
        async with session.get(
            URL,
            headers=_headers,
            params={k: v for k, v in params.items() if v is not None},
        ) as resp:
            if resp.status == HTTPStatus.TOO_MANY_REQUESTS:
                log.warning("API exceeded rate limit.")
                async with _lock:
                    _limit = 0
                    _reset = time() + float(resp.headers["Retry-After"])
            elif "RateLimit-Remaining" in resp.headers and "RateLimit-Reset" in resp.headers:
                async with _lock:
                    _limit = int(resp.headers["RateLimit-Remaining"])
                    _reset = time() + float(resp.headers["RateLimit-Reset"])
            else:
                log.warning("API response contained no rate limit information.")
            if "X-Pin" in resp.headers:
                _headers["X-Pin"] = resp.headers["X-Pin"]
            if "X-Autologin" in resp.headers:
                _headers["X-Autologin"] = resp.headers["X-Autologin"]
            if resp.status == HTTPStatus.NOT_FOUND:
                return None
            resp.raise_for_status()
            return await resp.text()
