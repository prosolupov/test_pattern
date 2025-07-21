from src.queue.fifo_queue import FifoQueue
from src.queue.priority_queue import PriorityQueue
from src.services.pattern_chain_of_responsibility.module.module_chain_enrichment import ModuleChainEnrichment
from src.services.pattern_chain_of_responsibility.module.module_chain_feeds import ModuleChainFeeds
from src.services.pattern_chain_of_responsibility.pipeline_chain import PipelineChain

if __name__ == '__main__':
    pipeline_one = PipelineChain()
    pipeline_one.add_module(ModuleChainEnrichment())

    pipeline_two = PipelineChain()
    pipeline_two.add_module(ModuleChainFeeds())

    #Создаём очередь по приоритетам
    queue = PriorityQueue()
    queue.enqueue_with_priority(1, pipeline_two)
    queue.enqueue_with_priority(2, pipeline_one)

    #Очередь FIFO
    fifo_queue = FifoQueue()
    fifo_queue.add_element(pipeline_one)
    fifo_queue.add_element(pipeline_two)

    print(fifo_queue.get_element.handle())