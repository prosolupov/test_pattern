from typing import Optional

from src.pattern_chain_of_responsibility.module.module_chain import ModuleChain


class PipelineChain:
    """
    Класс pipeline формирует цепочку модулей и запускает модули на выполнение
    """

    def __init__(self):
        self.first_module = None
        self.request = None

    def add_module(self, module: ModuleChain):
        if not self.first_module:
            self.first_module = module
        else:
            current = self.first_module
            while getattr(current, '_next_module', None):
                current = current._next_module
            current.set_next(module)

    def set_request(self, request: str):
        self.request = request
        # Пробросим запрос во все модули
        current = self.first_module
        while current:
            current.request = request
            current = getattr(current, '_next_module', None)

    def handle(self) -> Optional[str]:
        if self.first_module:
            return self.first_module.handle()
        return None
