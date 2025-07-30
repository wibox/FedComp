from fedcomp.aggregation.entities import AggregatedModel
from fedcomp.aggregation.base_aggregator import BaseAggregator

class Aggregator(BaseAggregator):

    def __init__(self) -> None:
        pass

    def aggregate(self) -> AggregatedModel:
        return AggregatedModel()