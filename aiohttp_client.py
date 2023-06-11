import aiohttp
import aiohttp.client_ws
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        ws: aiohttp.client_ws.ClientWebSocketResponse
        async with session.ws_connect('http://localhost:8765/test') as ws:
            await asyncio.sleep(12)
            await ws.receive_str()

asyncio.run(main())
