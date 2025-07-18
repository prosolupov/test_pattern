from abc import ABC, abstractmethod


class ModuleCommand(ABC):
    """
    Абстрактный класс модуля
    """
    @abstractmethod
    def execute(self) -> None:
        pass
