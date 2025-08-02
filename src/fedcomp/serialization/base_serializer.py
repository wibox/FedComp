from abc import ABC, abstractmethod
from typing import Any, Callable, Dict


class BaseSerializer(ABC):
    """Base serialization class from which actual serializers should inherit for compatibility.

    Args:
        serialization_protocols : typing.Dict[str, typing.Callable] = Dict of serialization protocols and respective serialization and deserialization methods supported by the Serializer.

        deserialization_protocols : typing.Dict[str, typing.Callable] = Dict of deserialization protocols and respective serialization and deserialization methods supported by the Serializer.
    """

    def __init__(
        self,
        serialization_protocols: Dict[str, Callable],
        deserialization_protocols: Dict[str, Callable],
    ) -> None:
        self.serialization_protocols = serialization_protocols
        self.deserialization_protocols = deserialization_protocols

    @classmethod
    @abstractmethod
    def serialize(cls, serilization_protocol: str, model: Any) -> Any:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def deserialize(cls, serialization_protocol: str, model: Any) -> Any:
        raise NotImplementedError
