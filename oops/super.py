# Base class
class Animal:
    def __init__(self, name):
        print(f"Initializing Animal: {name}")
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


# Intermediate class 1 inheriting from Animal
class Mammal(Animal):
    def __init__(self, name, fur_color):
        # Using super() to call the __init__ of the next class in the MRO (Animal in this case)
        print(f"Initializing Mammal: {name}, Fur Color: {fur_color}")
        super().__init__(name)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} gives birth to live young.")


# Intermediate class 2 inheriting from Animal
class Bird(Animal):
    def __init__(self, name, wing_span):
        # Using super() to call the __init__ of the next class in the MRO (Animal in this case)
        print(f"Initializing Bird: {name}, Wing Span: {wing_span} cm")
        super().__init__(name)
        self.wing_span = wing_span

    def lay_eggs(self):
        print(f"{self.name} lays eggs.")


# Derived class inheriting from both Mammal and Bird - this creates the diamond structure
# Animal
#  /    \
# Mammal Bird
#  \    /
#   Bat
class Bat(Bird, Mammal):
    def __init__(self, name, fur_color, wing_span, nocturnal=True):
        print(f"Initializing Bat: {name}, Nocturnal: {nocturnal}")
        # Using super() here is crucial.
        # In Python 3, super() correctly uses the Method Resolution Order (MRO)
        # to call the __init__ methods of Mammal and then Bird (and finally Animal)
        # in the correct sequence, ensuring each parent's __init__ is called exactly once.
        super().__init__(name, fur_color=fur_color, wing_span=wing_span)
        self.nocturnal = nocturnal

    def fly(self):
        print(f"{self.name} flies using its wings.")

    # Override speak method
    def speak(self):
        print(f"{self.name} squeaks.")


# --- Demonstration ---

# print("--- Creating Bird Instance ---")
# my_bird = Bird("Birdy", wing_span=30)
#
# my_bird.speak()
# my_bird.lay_eggs()

# Create an instance of Bat
print("--- Creating Bat Instance ---")
my_bat = Bat("Barty", fur_color="Brown", wing_span=30)

print("\n--- Bat Properties and Methods ---")
print(f"Name: {my_bat.name}")
print(f"Fur Color: {my_bat.fur_color}")
print(f"Wing Span: {my_bat.wing_span} cm")
print(f"Nocturnal: {my_bat.nocturnal}")
#
# my_bat.speak()
# my_bat.give_birth()  # Inherited from Mammal
# my_bat.lay_eggs()  # Inherited from Bird (even though bats are mammals, this shows inheritance path)
# my_bat.fly()  # Defined in Bat
#
# print("\n--- Method Resolution Order (MRO) for Bat ---")
# # The MRO shows the order in which Python looks for methods and attributes.
# # super() follows this order.
# print(Bat.__mro__)

# --- Explanation of the Diamond Problem and Super() ---
# The "diamond problem" occurs in multiple inheritance when a class inherits
# from two classes that have a common ancestor. In our example:
# Animal is the common ancestor of Mammal and Bird, and Bat inherits from both.
#
# The problem is how to handle the initialization or method calls from the
# common ancestor (`Animal.__init__` or `Animal.speak`). Without a proper
# mechanism, the ancestor's method might be called multiple times or not at all
# in the correct sequence.
#
# In Python 3, the `super()` function solves this problem using the C3
# linearization algorithm to determine the Method Resolution Order (MRO).
#
# When `super().__init__(...)` is called in `Bat`, it doesn't just call the
# `__init__` of the *immediate* parent classes (`Mammal` and `Bird` directly).
# Instead, it calls the `__init__` of the *next class* in the MRO.
#
# Let's trace the Bat initialization with super():
# 1. `Bat.__init__` is called.
# 2. `super().__init__(name, fur_color=fur_color, wing_span=wing_span)` is called within `Bat.__init__`.
# 3. `super()` in `Bat` points to `Mammal` (the first class in Bat's MRO after Bat).
# 4. `Mammal.__init__(name, fur_color)` is called.
# 5. Inside `Mammal.__init__`, `super().__init__(name)` is called.
# 6. `super()` in `Mammal` points to `Bird` (the next class in Bat's MRO after Mammal).
#    *Note: Even though Mammal's direct parent is Animal, super() follows the MRO of the *instance* (Bat).*
# 7. `Bird.__init__(name, wing_span)` is called.
# 8. Inside `Bird.__init__`, `super().__init__(name)` is called.
# 9. `super()` in `Bird` points to `Animal` (the next class in Bat's MRO after Bird).
# 10. `Animal.__init__(name)` is called.
# 11. After `Animal.__init__` completes, control returns to `Bird.__init__`.
# 12. After `Bird.__init__` completes, control returns to `Mammal.__init__`.
# 13. After `Mammal.__init__` completes, control returns to `Bat.__init__`.
# 14. `Bat.__init__` finishes.
#
# This ensures that `Animal.__init__` is called only once, and the initializers
# of `Mammal` and `Bird` are called in the order specified by the MRO,
# correctly handling the shared parent.

# --- Incorrect approach without super() in Python 3 (for demonstration) ---
# If you were to explicitly call parent __init__ methods like this (DON'T DO THIS in Python 3 multiple inheritance):
# class Bat_Incorrect(Mammal, Bird):
#     def __init__(self, name, fur_color, wing_span, nocturnal=True):
#         print(f"Initializing Bat_Incorrect: {name}")
#         Mammal.__init__(self, name, fur_color) # Calls Mammal's init, which calls Animal's init
#         Bird.__init__(self, name, wing_span)   # Calls Bird's init, which calls Animal's init AGAIN
#         self.nocturnal = nocturnal
# # Creating an instance would call Animal.__init__ twice, which is usually undesirable.
# # incorrect_bat = Bat_Incorrect("Bad Bat", fur_color="Black", wing_span=25)
