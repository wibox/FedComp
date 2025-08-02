from pydantic import BaseModel


class Client(BaseModel):
    ip: str
