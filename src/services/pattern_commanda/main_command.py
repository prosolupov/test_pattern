from src.services.pattern_commanda.module.module_command_enrichment import ModuleCommandEnrichment
from src.services.pattern_commanda.module.module_command_feeds import ModuleCommandFeeds
from src.services.pattern_commanda.pipeline_commanda import PipelineCommanda

if __name__ == '__main__':
    pipeline = PipelineCommanda()
    pipeline.add_module(ModuleCommandEnrichment())
    pipeline.add_module(ModuleCommandFeeds())

    pipeline.run("Start")