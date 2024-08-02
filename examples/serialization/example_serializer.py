from fedcomp.serialization.base_serializer import BaseSerializer

import traceback
import typing

import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np

class Cnn(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def _json_serialization(model : typing.Any) -> typing.Union[typing.Any, None]:
    _serialized_model = None
    try:
        _serialized_model = {name: param.detach().cpu().numpy().tolist() for name, param in model.state_dict().items()}
        if len(_serialized_model.keys()) != len([_ for _ in model.state_dict().keys()]):
            raise Exception
    except Exception as e:
        print(traceback.print_exc())
        return _serialized_model
    finally:
        return _serialized_model
    
def _json_deserialization(serialized_model : typing.Any, model_name : str) -> typing.Union[typing.Any, None]:
    state_dict = {}
    _deserialized_model = None
    try:
        if serialized_model is None:
            raise Exception
        for name, value_list in serialized_model.items():
            tensor_data = np.array(value_list)
            tensor = torch.tensor(tensor_data)
            state_dict[name] = tensor
    except Exception as e:
        print(traceback.print_exc())
        return _deserialized_model
    finally:
        try:
            # HERE YOUR MODEL SHOULD BE APPROPRIATELY INITIALIZED
            # A RANDOM STATE IS SUGGESTED AS IT AVOIDS LOADING TIMES
            # PARAMETERS WILL BE REPLACED VIA THE DESERIALIZATION PROCESS ANYWAY
            nn = Cnn()
            incompatible_keys = nn.load_state_dict(state_dict=state_dict)
            if len(incompatible_keys[0]) > 0 or len(incompatible_keys[1]) > 0:
                raise Exception
            _deserialized_model = nn
            return _deserialized_model
        except Exception as e:
            print(traceback.print_exc())
            return _deserialized_model
        finally:
            return _deserialized_model

class Serializer(BaseSerializer):
    def __init__(
        self,
        serialization_protocols: typing.Dict[str, typing.Callable],
        deserialization_protocols: typing.Dict[str, typing.Callable]
    ) -> None:
        super().__init__(serialization_protocols, deserialization_protocols)
        
    def serialize(self, serialization_protocol : str, model : typing.Any) -> typing.Any:
        if serialization_protocol not in self.serialization_protocols:
            raise Exception()
        else:
            return self.serialization_protocols[serialization_protocol](model)
    
    def deserialize(self, serialization_protocol : str, model : typing.Any) -> typing.Any:
        if serialization_protocol not in self.deserialization_protocols:
            raise Exception
        else:
            return self.deserialization_protocols[serialization_protocol](model)
        
serialization_protocols = {"json":_json_serialization.__func__}
deserialization_protocols = {"json":_json_deserialization.__func__}

my_serializer = Serializer(serialization_protocols, deserialization_protocols)
nn = Cnn()

json_model = my_serializer.serialize("json", nn)
original_modle = my_serializer.deserialize("json", json_model)