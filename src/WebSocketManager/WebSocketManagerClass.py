import asyncio
import functools
import json
import threading

import websockets
from typing import Callable, Any

class WebSocketManager:
    def __init__(self, host: str="localhost", port: int=8080):
        self.host = host
        self.port = port
        self.link = f"ws://{host}:{port}"
        self.execute_on_recv = []

    def on_recv(self, func:Callable):

        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        self.execute_on_recv.append(func)

        return func

    async def start(self):
        raise NotImplementedError

    def run(self):
        asyncio.run(self.start())

    def run_in_thread(self):
        thread = threading.Thread(target=self.start, daemon=True)
        thread.start()



