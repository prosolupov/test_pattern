from src.pattern_strategy.module.module_enrichment import ModuleEnrich
from src.pattern_strategy.module.module_feeds import ModuleFeeds
from src.pattern_strategy.pypline_strategy import PyplineStrategy

if __name__ == '__main__':
   con: list = [ModuleEnrich, ModuleFeeds]
   pypline = PyplineStrategy(con)
   pypline.run_logic()