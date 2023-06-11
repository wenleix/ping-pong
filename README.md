# Start Uvicorn Server
```
uvicorn app:app --port 8765 --ws-ping-interval 5 --ws-ping-timeout 5
```

# Run aiohttp Websocket Client
python aiohttp_client.py

# Result
Server side stacktrace:
```
Traceback (most recent call last):
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/uvicorn/protocols/websockets/websockets_impl.py", line 238, in run_asgi
    result = await self.app(self.scope, self.asgi_receive, self.asgi_send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/uvicorn/middleware/proxy_headers.py", line 78, in __call__
    return await self.app(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/fastapi/applications.py", line 271, in __call__
    await super().__call__(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/applications.py", line 118, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/middleware/errors.py", line 149, in __call__
    await self.app(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 79, in __call__
    raise exc
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 68, in __call__
    await self.app(scope, receive, sender)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/fastapi/middleware/asyncexitstack.py", line 21, in __call__
    raise e
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/routing.py", line 706, in __call__
    await route.handle(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/routing.py", line 341, in handle
    await self.app(scope, receive, send)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/routing.py", line 82, in app
    await func(session)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/fastapi/routing.py", line 289, in app
    await dependant.call(**values)
  File "/Users/wx/code/ping_pong/./app.py", line 12, in test
    await websocket.send_text("Hello")
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/websockets.py", line 163, in send_text
    await self.send({"type": "websocket.send", "text": data})
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/websockets.py", line 85, in send
    await self._send(message)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/starlette/middleware/exceptions.py", line 65, in sender
    await send(message)
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/uvicorn/protocols/websockets/websockets_impl.py", line 311, in asgi_send
    await self.send(data)  # type: ignore[arg-type]
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/websockets/legacy/protocol.py", line 635, in send
    await self.ensure_open()
  File "/Users/wx/.pyenv/versions/3.9.13/envs/ping-pong/lib/python3.9/site-packages/websockets/legacy/protocol.py", line 935, in ensure_open
    raise self.connection_closed_exc()
websockets.exceptions.ConnectionClosedError: sent 1011 (unexpected error) keepalive ping timeout; no close frame received
```

Client side stacktrace shows aiohttp websocket client start to respond with pong after 12 seconds, upon the `receive_str` call:
```
Traceback (most recent call last):
  File "/Users/wx/code/ping_pong/aiohttp_client.py", line 12, in <module>
    asyncio.run(main())
  File "/Users/wx/.pyenv/versions/3.9.13/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/Users/wx/.pyenv/versions/3.9.13/lib/python3.9/asyncio/base_events.py", line 647, in run_until_complete
    return future.result()
  File "/Users/wx/code/ping_pong/aiohttp_client.py", line 10, in main
    await ws.receive_str()
  File "/Users/wx/.pyenv/versions/ping-pong/lib/python3.9/site-packages/aiohttp/client_ws.py", line 273, in receive_str
    msg = await self.receive(timeout)
  File "/Users/wx/.pyenv/versions/ping-pong/lib/python3.9/site-packages/aiohttp/client_ws.py", line 265, in receive
    await self.pong(msg.data)
  File "/Users/wx/.pyenv/versions/ping-pong/lib/python3.9/site-packages/aiohttp/client_ws.py", line 146, in pong
    await self._writer.pong(message)
  File "/Users/wx/.pyenv/versions/ping-pong/lib/python3.9/site-packages/aiohttp/http_websocket.py", line 670, in pong
    await self._send_frame(message, WSMsgType.PONG)
  File "/Users/wx/.pyenv/versions/ping-pong/lib/python3.9/site-packages/aiohttp/http_websocket.py", line 646, in _send_frame
    self._write(header + mask + message)
  File "/Users/wx/.pyenv/versions/ping-pong/lib/python3.9/site-packages/aiohttp/http_websocket.py", line 663, in _write
    raise ConnectionResetError("Cannot write to closing transport")
ConnectionResetError: Cannot write to closing transport
```

# Test Result for [websockets](https://pypi.org/project/websockets/) Library with DEBUG log:
```
python websocket_client.py
```

Execution succeed, and the logs shows `websockets` was able to respond to Ping request during non-block call:
```
...
DEBUG:websockets.client:< PING 42 76 ad d3 [binary, 4 bytes]
DEBUG:websockets.client:> PONG 42 76 ad d3 [binary, 4 bytes]
DEBUG:websockets.client:< PING d5 de 26 93 [binary, 4 bytes]
DEBUG:websockets.client:> PONG d5 de 26 93 [binary, 4 bytes]
DEBUG:websockets.client:< TEXT 'Hello' [5 bytes]
INFO:__main__:Hello
...
```
