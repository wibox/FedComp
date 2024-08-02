from abc import ABC, abstractmethod

import typing

class BaseSerializer(ABC):
    """Base serialization class from which actual serializers should inherit for compatibility.

    Args:
        serialization_protocols : typing.Dict[str, typing.Callable] = Dict of serialization protocols and respective serialization and deserialization methods supported by the Serializer.
        
        deserialization_protocols : typing.Dict[str, typing.Callable] = Dict of serialization protocols and respective serialization and deserialization methods supported by the Serializer.
    """
    def __init__(
        self,
        serialization_protocols : typing.Dict[str, typing.Callable],
        deserialization_protocols : typing.Dict[str, typing.Callable]
    ) -> None:
        self.serialization_protocols = serialization_protocols
        self.deserialization_protocols = deserialization_protocols
        
    @classmethod
    @abstractmethod
    def serialize(self, serilization_protocol : str, model : typing.Any) -> typing.Any:
        raise NotImplementedError
    
    @classmethod
    @abstractmethod
    def deserialize(self, serialization_protocol : str, model : typing.Any) -> typing.Any:
        raise NotImplementedError