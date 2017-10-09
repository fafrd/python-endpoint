# python-endpoint

Wrapper code for handling an incoming http request using gevent.

The example here will just return the request as json. modify the process() method as needed.

starting:
```
python endpoint.py
```
calling with curl:
```
curl localhost:4111 -d "hi"
{"request": "hi"}
```
