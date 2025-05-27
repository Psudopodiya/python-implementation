class Dog:
    species = "Canis Firmilia"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    # def __repr__(self):
    #     pass

    # def __str__(self):
    #     return f"{self.name} is {self.age} years old"


miles = Dog("miles", 23)
#without __str__ gives more object like response <__main__.Dog object at 0x101040c10>
print(miles)




