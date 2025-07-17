from src.pattern_chain_of_responsibility.module.module_chain import ModuleChain


class BaseModuleChain(ModuleChain):
    """
    Базовая реализация модуля
    """

    def __init__(self):
        self._next_module = None

    def set_next(self, module: ModuleChain) -> ModuleChain:
        self._next_module = module
        return module

    def handle(self) -> str:
        result = self.__class__.__name__
        if self._next_module:
            result += " -> " + self._next_module.handle()
        return result
