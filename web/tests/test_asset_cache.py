import threading
import re
from types import SimpleNamespace
from urllib.error import HTTPError
from urllib.request import build_opener,ProxyHandler
from web.__main__ import make_server


def test_static_assets_cache_while_html_and_ticket_state_do_not():
    server=make_server(SimpleNamespace(state=lambda:{'synthetic':True},stations=[]),port=0)
    thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
    client=build_opener(ProxyHandler({}));base='http://127.0.0.1:'+str(server.server_port)
    try:
        with client.open(base+'/') as response:
            html=response.read().decode();assert 'no-store' in response.headers['Cache-Control']
        url=re.search(r'src="([^"]+asset_version=[^"]+)"',html)[1]
        with client.open(base+url) as response:
            response.read();assert 'immutable' in response.headers['Cache-Control'];etag=response.headers['ETag']
        from urllib.request import Request
        try:
            client.open(Request(base+url,headers={'If-None-Match':etag}))
        except HTTPError as response:
            assert response.code==304
        else:raise AssertionError('Expected conditional static response')
        with client.open(base+'/api/state') as response:assert response.headers['Cache-Control']=='no-store'
    finally:
        server.shutdown();server.server_close();thread.join(2)
