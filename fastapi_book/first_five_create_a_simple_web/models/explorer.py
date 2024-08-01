from pydantic import BaseModel

class Explorers(BaseModel):
    name:str
    country : str
    description : str