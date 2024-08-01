from fastapi import APIRouter
from models.explorer import Explorers
from fake import explorer as service

router = APIRouter(prefix="/explorer")


@router.get("/")
def get_all() -> list[Explorers]:
    return service.get_all_explorers()


@router.get("/{name}")
def get_one(name) -> Explorers | None:
    return service.get_one_explorer(name)


@router.post("/")
def create(explorer: Explorers) -> Explorers:
    return service.create_explorer(explorer)


@router.patch("/")
def modify(explorer: Explorers) -> Explorers:
    return service.modify_explorer(explorer)


@router.put("/")
def replace(explorer: Explorers) -> Explorers:
    return service.replace_explorer(explorer)


@router.delete("/{name}")
def delete(name: str):
    return None
