import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:6969") as websocket:
        while True:
            user_input = input("Enter message to send to server (or 'exit' to quit): ")
            await websocket.send(user_input)
            
            if user_input.lower() == "exit":
                break
            
            response = await websocket.recv()
            print(f"Received response: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
