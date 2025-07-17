from abc import ABC, abstractmethod
from typing import Optional, Any


class ModuleChain(ABC):
    """
    Абстрактный класс модуля
    """

    @abstractmethod
    def set_next(self, module: 'ModuleChain') -> 'ModuleChain':
        pass

    @abstractmethod
    def handle(self) -> Optional[str]:
        pass
