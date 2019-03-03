import pytest
from aiohttp import web
from mock import mock

from v1.gis_service.mocks import get_or_create
from v1.gis_service.loader import Loader


@pytest.fixture
def cli(loop, aiohttp_client):
    loader = Loader()
    app = web.Application()
    app.add_routes(loader.url_routes)
    return loop.run_until_complete(aiohttp_client(app))


# async def test_set_value(cli):
#     resp = await cli.post('/', data={'value': 'foo'})
#     assert resp.status == 200
#     assert await resp.text() == 'thanks for the data'
#     assert cli.server.app['value'] == 'foo'


@mock.patch('peewee_async.Manager.get_or_create', side_effect=get_or_create)
async def test_get_value(cli):
    cli.server.app['value'] = 'bar'
    resp = await cli.get('/')
    assert resp.status == 200
    assert await resp.text() == 'value: bar'
