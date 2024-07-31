from models import Creature
from fastapi import FastAPI
from typing import List

app = FastAPI()


@app.get("/creatures", response_model=List[Creature])
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()
