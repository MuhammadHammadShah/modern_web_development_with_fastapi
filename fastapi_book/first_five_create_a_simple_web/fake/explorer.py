from models.explorer import Explorers

_explorers = [Explorers(name="khan", country="USA", description="not a king"), Explorers(
    name="khan", country="USA", description="not a king")]


def get_all_explorers() -> list[Explorers]:
    return _explorers


def get_one_explorer(name) -> Explorers:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


def create_explorer(explorer: Explorers) -> Explorers:
    return explorer


def modify_explorer(explorer: Explorers) -> Explorers:
    return explorer


def replace_explorer(explorer: Explorers) -> Explorers:
    return explorer


def replace_explorer(explorer: Explorers) -> Explorers:
    return explorer


def delete(explorer: Explorers) -> Explorers:
    return explorer
