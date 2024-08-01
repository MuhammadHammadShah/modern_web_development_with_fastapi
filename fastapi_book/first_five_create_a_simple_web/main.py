from fastapi import FastAPI, APIRouter
from web import explorer, creature

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)


@app.get("/")
def home():
    return f"I am from home at main.py"
