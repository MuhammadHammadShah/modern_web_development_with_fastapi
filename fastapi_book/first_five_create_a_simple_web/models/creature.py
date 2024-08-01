from pydantic import BaseModel


class Creatures(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str
