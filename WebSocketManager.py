import asyncio
import functools
import json
import threading

import websockets
from typing import Callable, Any


class WebSocketManager:
    def __init__(self, port:int):
        self.port: int = port
        self.handlers: dict[tuple, Callable] = {}
        self.websocket = None

    def on_recv(self, key: str, value: Any):
        def decorator(func: Callable):

            self.handlers[(key, value)] = func
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)

            return wrapper
        return decorator

    async def start(self):
        async with websockets.connect(f"ws://localhost:{self.port}") as websocket:
            while True:
                message = await websocket.recv()
                if not message:
                    continue
                message = json.loads(message)
                for (key, value), func in self.handlers.items():
                    match = message.get(key)
                    if not match: continue
                    if match == value:
                        await func(message)

    def run_in_thread(self):
        thread = threading.Thread(target=self.start, daemon=True)
        thread.start()



