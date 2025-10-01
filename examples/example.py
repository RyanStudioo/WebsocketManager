from WebSocketManager import WebSocketClient, ClientConnection
import json

ws = WebSocketClient(host='localhost', port=8080)

@ws.on_recv
async def testing(websocket:ClientConnection, message:dict):
    print(message)

print("starting")
ws.run()