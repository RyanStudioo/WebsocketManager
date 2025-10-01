from .WebSocketManagerClass import WebSocketManager


class WebSocketServer(WebSocketManager):
    def __init__(self, host='127.0.0.1', port=8080):
        super().__init__(host, port)

    async def start(self):
        pass