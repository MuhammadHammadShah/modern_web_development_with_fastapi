from models import Creature

a_creatures: list[Creature] = [
    Creature(name="yeti", country="USA", area="Himalayas",
             description="From Himalayas", aka="Abominable Snowman"),
    Creature(name="Golem", country="UK", area="London",
             description="from Dark Barracks", aka="Bigfoot_boy"),
]


def get_creatures() -> list[Creature]:
    return a_creatures
