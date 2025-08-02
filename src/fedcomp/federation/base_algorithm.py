from abc import ABC, abstractmethod
from entities import UpdatedModel


class BaseAlgorithm:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def average_models() -> UpdatedModel:
        pass
