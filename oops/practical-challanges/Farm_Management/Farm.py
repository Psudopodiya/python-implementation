from abc import ABC, abstractmethod
from typing import List


class Food:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name}: {self.weight} kg"


class Animal(ABC):

    def __init__(self, name: str, age: int, weight: float, preferred_foods: List[str]):
        self.name = name
        self.age = age
        self.weight = weight
        self.preferred_foods = preferred_foods

    @abstractmethod
    def make_sound(self) -> str:
        pass

    def feed(self, food) -> None:
        pass

    @abstractmethod
    def produce(self) -> str or None:
        pass


class Cow(Animal):
    def __init__(self, name, age, weight, preferred_foods=None):
        if preferred_foods is None:
            preferred_foods = ['grass', "hay"]
        super().__init__(name, age, weight, preferred_foods)

    def make_sound(self):
        return "Moo"

    def feed(self, food):
        if food.name.lower() not in self.preferred_foods:
            print(f"Cannot feed {food} to {self.name}")

        self.weight += food.weight
        return

    def produce(self):
        return "Milk"

    def __str__(self):
        return f"Cow - {self.name} ({self.weight})kg"


class Hen(Animal):
    def __init__(self, name, age, weight, preferred_foods=None):
        if preferred_foods is None:
            preferred_foods = ['corn', "wheat"]
        super().__init__(name, age, weight, preferred_foods)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if food.name.lower() not in self.preferred_foods:
            print(f"Cannot feed {food} to {self.name}")

        self.weight += food.weight
        return

    def produce(self):
        return "Egg"

    def __str__(self):
        return f"Hen - {self.name} ({self.weight})kg"


class Sheep(Animal):
    def __init__(self, name, age, weight, preferred_foods=None):
        if preferred_foods is None:
            preferred_foods = ['grass']
        super().__init__(name, age, weight, preferred_foods)

    def make_sound(self):
        return "Baa"

    def feed(self, food):
        if food.name.lower() not in self.preferred_foods:
            print(f"Cannot feed {food} to {self.name}")

        self.weight += food.weight
        return

    def produce(self):
        return "Wool"

    def __str__(self):
        return f"Hen - {self.name} ({self.weight})kg"


class Dog(Animal):
    def __init__(self, name, age, weight, preferred_foods=None):
        if preferred_foods is None:
            preferred_foods = ["meat", "bone"]
        super().__init__(name, age, weight, preferred_foods)

    def make_sound(self):
        return "Woof"

    def feed(self, food):
        if food.name.lower() not in self.preferred_foods:
            print(f"Cannot feed {food} to {self.name}")
            return
        self.weight += food.weight
        return

    def produce(self):
        return None

    def __str__(self):
        return f"Hen - {self.name} ({self.weight})kg"


class Farm:

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all(self, food: Food):
        if len(self.animals) == 0:
            print("No animals in the farm")
            return
        for animal in self.animals:
            animal.feed(food)
        print("Fed all animals")
        return

    def collect_all_produce(self) -> List[str]:
        collected_produce = []
        for animal in self.animals:
            collected_produce.append(animal.collect_produce())
        return collected_produce

    def farm_report(self):
        for animal in self.animals:
            print(animal)
