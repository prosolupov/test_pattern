from src.services.pattern_chain_of_responsibility.module.module_chain_enrichment import ModuleChainEnrichment
from src.services.pattern_chain_of_responsibility.module.module_chain_feeds import ModuleChainFeeds
from src.services.pattern_chain_of_responsibility.pipeline_chain import PipelineChain

if __name__ == '__main__':
    pipeline = PipelineChain()

    pipeline.add_module(ModuleChainEnrichment())
    pipeline.add_module(ModuleChainFeeds())

    print(pipeline.handle())
