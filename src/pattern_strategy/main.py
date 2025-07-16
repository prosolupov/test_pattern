from http import HTTPStatus

from src.pattern_strategy.models.module.module_enrichment import ModuleEnrich
from src.pattern_strategy.models.module.module_feeds import ModuleFeeds
from src.pattern_strategy.models.pypline import Pypline

if __name__ == '__main__':
   con: list = [ModuleEnrich, ModuleFeeds]
   pypline = Pypline(con)
   pypline.run_logic()