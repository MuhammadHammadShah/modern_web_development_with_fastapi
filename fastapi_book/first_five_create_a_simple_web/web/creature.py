from fastapi import APIRouter
from models.creature import Creatures
from fake import creature as service

router = APIRouter(prefix="/creature")


@router.get("/")
def get_all() -> list[Creatures]:
    return service.get_all_creature


@router.get("/{name}")
def get_one(name) -> Creatures | None:
    return service.get_one_creature(name)


@router.post("/")
def create(creature: Creatures) -> Creatures:
    return service.create_creature(creature)


@router.patch("/")
def modify(creature: Creatures) -> Creatures:
    return service.modify_creature(creature)


@router.put("/")
def replace(creature: Creatures) -> Creatures:
    return service.replace_creature(creature)


@router.delete("/{name}")
def delete(name: str):
    return None
