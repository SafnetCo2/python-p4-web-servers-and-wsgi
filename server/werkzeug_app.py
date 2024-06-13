#!/usr/bin/env python3
from werkzeug.wrappers import Request,Response

@Request.application
def application(request):
    print(f'server running at {request.remote_addr}')
    return Response('A werkzeung generated request')
if __name__=='__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )
