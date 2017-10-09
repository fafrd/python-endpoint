#!/usr/bin/env python
import sys, json, time, gevent
from gevent import socket, pywsgi, monkey; monkey.patch_all() #monkey patch python to allow concurrency
reload(sys)
sys.setdefaultencoding('utf8') #hack to get utf8 working properly
port = 4111

def process(incoming):
    results = incoming
    return json.dumps({"request": incoming})

def handleRequest(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    yield process(environ['wsgi.input'].read())

print('Server ready.')
server = pywsgi.WSGIServer(('', port), handleRequest)
server.serve_forever()
