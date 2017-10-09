# python-endpoint

Wrapper code for handling an incoming http request using gevent.
This code should work concurrently; a thread will be spawned for each incoming connection.

## usage
The example here will just return the request as json. modify the process() method as needed.
```
python endpoint.py
```
calling with curl:
```
curl localhost:4111 -d "hi"
{"request": "hi"}
```
