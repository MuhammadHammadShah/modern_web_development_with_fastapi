from models.explorer import Explorers
import fake.explorer as data


def get_all() -> list[Explorers]:
    return data.get_all_creature()


def get_one(name: str) -> Explorers | None:
    return data.get_one_explorer(name)


def create(explorer: str) -> Explorers:
    return data.create_explorer(explorer)


def replace(id, explorer: Explorers) -> Explorers:
    return data.replace_explorer(id, explorer)


def modify(id, explorer: Explorers) -> Explorers:
    return data.modify__explorer(id, explorer)


def delete(id, creature: Explorers) -> bool:
    return data.delete_explorer(id)
