from models.creature import Creatures

_creatures = [Creatures(name="khanbaba", country="USA", area="LosAngeles", description="not a king", aka="nothing"), Creatures(
    name="khanbaba", country="USA", area="LosAngeles", description="not a king", aka="nothing")]


def get_all_creature() -> list[Creatures]:
    return _creatures


def get_one_creature(name) -> Creatures:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


def create_creature(creature: Creatures) -> Creatures:
    return creature


def modify_creature(creature: Creatures) -> Creatures:
    return creature


def replace_creature(creature: Creatures) -> Creatures:
    return creature


def replace_creature(creature: Creatures) -> Creatures:
    return creature


def delete_creature(creature: Creatures) -> Creatures:
    return creature
