from typing import Callable, Any

class Executable:
    def __init__(self, func:Callable):
        self.func = func

class ExecutableHandler(Executable):
    def __init__(self, func:Callable, key:str=None, value:Any=None, ensure:bool=False):
        super().__init__(func)
        self.key = key
        self.value = value
        self.ensure = ensure