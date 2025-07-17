from http import HTTPStatus

from src.pattern_strategy.services.module.module import Module


class Pypline:
    """
    Класс Pypline для запуска и выполнения модулей
    """
    def __init__(self, context: list[Module]) -> None:
        self._context: list = context

    @property
    def context_object(self) -> list[Module]:
        return self._context

    @context_object.setter
    def context_object(self, context: Module) -> None:
        self._context = context

    def run_logic(self) -> None:
        for con in self._context:
            try:
                con.my_logic(self)
            except BaseException as ex:
                print("HTTPStatus")