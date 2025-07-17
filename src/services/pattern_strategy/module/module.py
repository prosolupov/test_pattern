from abc import ABC, abstractmethod


class Module(ABC):
    """Базовый абстрактный класс"""

    @abstractmethod
    def my_logic(self) -> None:
        pass
