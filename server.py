import asyncio
import websockets

async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        response = f"Server received: {message}"
        await websocket.send(response)
        print(f"Sent response: {response}")

start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
