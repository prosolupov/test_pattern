from src.pattern_chain_of_responsibility.services.module.module_chain_enrichment import ModuleChainEnrichment
from src.pattern_chain_of_responsibility.services.module.module_chain_feeds import ModuleChainFeeds
from src.pattern_chain_of_responsibility.services.pipeline_chain import PipelineChain

if __name__ == '__main__':
    pipeline = PipelineChain()

    pipeline.add_module(ModuleChainEnrichment())
    pipeline.set_request("a")

    pipeline.add_module(ModuleChainFeeds())
    pipeline.set_request("b")

    print(pipeline.handle())