from .WebSocketManagerClass import WebSocketManager
import asyncio
import functools
import json
import threading
import websockets
from typing import Callable, Any

class WebSocketClient(WebSocketManager):
    def __init__(self, host='localhost', port=8080):
        super().__init__(host, port)

    async def start(self):
        async with websockets.connect(self.link) as websocket:
            while True:
                message = await websocket.recv()
                if not message:
                    continue
                message = json.loads(message)
                for executable in self.execute_on_recv:
                    await executable(websocket, message)
