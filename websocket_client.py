import websockets
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def main():
    async with websockets.connect('ws://localhost:8765/test') as websocket:
        await asyncio.sleep(12)
        val = await websocket.recv()
        logger.info(val)

asyncio.run(main())
