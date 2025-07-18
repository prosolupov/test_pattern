from src.services.pattern_commanda.module.module_command import ModuleCommand


class ModuleCommandEnrichment(ModuleCommand):
    """
    Модуль для реализации определенной логики
    """

    def execute(self) -> None:
        print("ModuleCommandEnrichment")