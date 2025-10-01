from WebSocketManager import WebSocketClient, ClientConnection
import json

ws = WebSocketClient(host='localhost', port=8080)

@ws.on_recv
async def testing(websocket:ClientConnection, message:dict):
    if message["type"] == "response":
        return
    print(message)
    await ws.send({"test": 1})

print("starting")
ws.run()