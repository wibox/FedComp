from abc import ABC, abstractmethod

from entities import AggregatedModel


class BaseAggregator(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def aggregate(self) -> AggregatedModel:
        raise NotImplementedError()
