from werkzeug.wrappers import Response
#without werkzeug application
# def application(environ,start_response):
#     start_response('200 OK',[('content-Type', 'text/plain')])
#     return['Hello World'.encode('utf-8')]

# with werkzeug application which helps you to access data directly to the 
#environment


#Here is how you would write that application with response objects:
from werkzeug.wrappers import Response
from werkzeug.serving import run_simple

def application(environ, start_response):
    response = Response('Hello World', mimetype='text/plain')
    return response(environ, start_response)

if __name__ == '__main__':
    run_simple('localhost', 5555, application, use_reloader=True, use_debugger=True)
