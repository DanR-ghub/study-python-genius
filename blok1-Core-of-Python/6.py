class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        print(f"{self.species} {self.name} видає звук!")

dog = Animal("Боб", "Собака", 3)
cat = Animal("Мурчик", "Кіт", 1)

dog.make_sound()
cat.make_sound()

#----------

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rect1 = Rectangle(4, 5)
rect2 = Rectangle(7, 3)

print(f"Площа першого прямокутника: {rect1.calculate_area()}")
print(f"Площа другого прямокутника: {rect2.calculate_area()}")
