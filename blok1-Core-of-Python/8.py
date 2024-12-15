from abc import ABC, abstractmethod

# Завдання 1: Інкапсуляція
class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password

    def set_name(self, name):
        self.__name = name
    
    def set_email(self, email):
        self.__email = email
    
    def set_password(self, password):
        self.__password = password


user1 = User("", "", "")

user1.set_name("Іван")
user1.set_email("ivan@example.com")
user1.set_password("securepassword")

print("Ім'я користувача:", user1.get_name())
print("Електронна пошта:", user1.get_email())
print("Пароль:", user1.get_password())

print("#==========================")
#==========================

# Завдання 2: Абстракція
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print("Площа кола:", circle.calculate_area())
print("Площа прямокутника:", rectangle.calculate_area())
print("Площа трикутника:", triangle.calculate_area())

#==========================

"""
Завдання 3: Аналіз коду 

Абстракція: Базовий клас забезпечує загальний інтерфейс для підключення до бази даних і виконання запитів, але не реалізує їх. Це роблять підкласи.
Інкапсуляція: Користувачі класів не знають, як саме виконується підключення до конкретної бази даних. Вони працюють через загальні методи, що спрощує взаємодію.

Переваги:
Читабельність: Код зрозумілий, оскільки всі бази даних мають однаковий інтерфейс.
Масштабованість: Додавання нового типу бази даних вимагає лише створення нового підкласу.
Безпека: Внутрішні деталі підключення приховані від користувача класу.

"""
