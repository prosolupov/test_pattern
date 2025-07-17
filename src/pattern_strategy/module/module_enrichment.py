from src.pattern_strategy.module.module import Module


class ModuleEnrich(Module):
    """
    Наследник от базового Модуля который реализует свою логику работы
    """
    def my_logic(self) -> None:
        print("ContextEnrich")
