from abc import ABC, abstractmethod


class Module(ABC):
    """Базовый абстрактный метод"""

    @abstractmethod
    def my_logic(self) -> None:
        pass
