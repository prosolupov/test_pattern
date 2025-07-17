import random
import time
from http import HTTPStatus

from src.pattern_strategy.module.module import Module


class ModuleFeeds(Module):
    """
    Наследник от базового Модуля который реализует свою логику работы
    """
    def my_logic(self) -> None:
        number = random.randint(1, 10)
        if number % 2 == 0:
            time.sleep(3)
            print("ContextFeeds")
        else:
            raise HTTPStatus.REQUEST_TIMEOUT