from typing import List, Any

from src.services.pattern_commanda.module.module_command import ModuleCommand


class PipelineCommanda:
    def __init__(self):
        self.modules: List[ModuleCommand] = []


    def add_module(self, module: ModuleCommand):
        self.modules.append(module)


    def run(self, initial_data: Any) -> Any:
        data = initial_data
        for module in self.modules:
            data = module.execute()
        return data