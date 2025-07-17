from abc import ABC, abstractmethod
from typing import Optional

from src.pattern_chain_of_responsibility.services.module.module_chain import ModuleChain


class PipelineChain(ABC):

    @abstractmethod
    def set_next(self, module: 'PipelineChain'):
        pass


    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass
