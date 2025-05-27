import pytest
from Farm import Farm, Cow, Hen, Sheep, Dog, Food

import pytest


# Assume all required classes are imported: Animal, Cow, Hen, Sheep, Dog, Food, Farm

@pytest.fixture
def setup_farm():
    farm = Farm("GreenField", "Iowa")

    cow = Cow("Daisy", 5, 250.0)
    hen = Hen("Clucky", 2, 3.0)
    sheep = Sheep("Wooly", 3, 55.0)
    dog = Dog("Rex", 4, 30.0)

    grass = Food("Grass", 10)
    hay = Food("Hay", 5)
    corn = Food("Corn", 3)
    wheat = Food("Wheat", 4)
    meat = Food("Meat", 2)
    rock = Food("Rock", 1)  # Invalid food for all

    for animal in [cow, hen, sheep, dog]:
        farm.add_animal(animal)

    return {
        "farm": farm,
        "animals": {"cow": cow, "hen": hen, "sheep": sheep, "dog": dog},
        "food": {"grass": grass, "hay": hay, "corn": corn, "wheat": wheat, "meat": meat, "rock": rock}
    }


def test_animal_sounds(setup_farm):
    assert setup_farm["animals"]["cow"].make_sound() == "Moo"
    assert setup_farm["animals"]["hen"].make_sound() == "Cluck"
    assert setup_farm["animals"]["sheep"].make_sound() == "Baa"
    assert setup_farm["animals"]["dog"].make_sound() == "Woof"


def test_feeding_preferred_food(setup_farm):
    cow = setup_farm["animals"]["cow"]
    before = cow.weight
    cow.feed(setup_farm["food"]["grass"])
    assert cow.weight > before


def test_feeding_unpreferred_food(setup_farm):
    hen = setup_farm["animals"]["hen"]
    before = hen.weight
    hen.feed(setup_farm["food"]["meat"])  # Not preferred
    assert hen.weight == before


def test_collect_produce(setup_farm):
    cow = setup_farm["animals"]["cow"]
    hen = setup_farm["animals"]["hen"]
    sheep = setup_farm["animals"]["sheep"]
    dog = setup_farm["animals"]["dog"]

    assert cow.produce() == "Milk"
    assert hen.produce() == "Egg"
    assert sheep.produce() == "Wool"
    assert dog.produce() is None


def test_feed_all_logic(setup_farm):
    farm = setup_farm["farm"]
    grass = setup_farm["food"]["grass"]
    cow_before = setup_farm["animals"]["cow"].weight
    sheep_before = setup_farm["animals"]["sheep"].weight

    farm.feed_all(grass)

    assert setup_farm["animals"]["cow"].weight > cow_before
    assert setup_farm["animals"]["sheep"].weight > sheep_before


def test_collect_all_produce(setup_farm):
    produce = setup_farm["farm"].collect_all_produce()
    assert "Milk" in produce
    assert "Egg" in produce
    assert "Wool" in produce
    assert None not in produce  # Dogs don't produce, but don't break logic


# def test_farm_report_output(setup_farm, capsys):
#     farm = setup_farm["farm"]
#     farm.print_farm_report()
#     output = capsys.readouterr().out
#     assert "Farm Report" in output or len(output.strip()) > 0


if __name__ == "__main__":
    import pytest

    pytest.main(["-v"])
