import aiohttp
from sanic.log import log
import warnings
from sanic.testing import TestClient

HOST = '127.0.0.1'
PORT = 42101

def sanic_endpoint_test(app, method='get', uri='/', gather_request=True,
                        debug=False, server_kwargs={},
                        *request_args, **request_kwargs):
    warnings.warn(
        "Use of sanic_endpoint_test will be deprecated in"
        "version 1.0.  Please use the `test_client` available"
        "on the app object.", DeprecationWarning)

    test_client = TestClient(app)
    return test_client._sanic_endpoint_test(
        method, uri, gather_request=gather_request, debug, server_kwargs
        *request_args, **request_kwargs)
