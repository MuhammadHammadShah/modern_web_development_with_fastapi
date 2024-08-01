from models.creature import Creatures
import fake.creature as data


def get_all() -> list[Creatures]:
    return data.get_all_creature()


def get_one(name: str) -> Creatures | None:
    return data.get_one_creature(name)


def create(creature: str) -> Creatures:
    return data.create_creature(creature)


def replace(id, creature: Creatures) -> Creatures:
    return data.replace_creature(id, creature)


def modify(id, creature: Creatures) -> Creatures:
    return data.modify__creature(id, creature)


def delete(id, creature: Creatures) -> bool:
    return data.delete_creature(id)
