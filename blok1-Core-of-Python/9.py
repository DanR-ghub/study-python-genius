from abc import ABC, abstractmethod

# Завдання 1: Принцип єдиного обов'язку (SRP)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_user(self):
        print(f"User '{self.name}' with email '{self.email}' has been created.")

    def update_user(self, new_name, new_email):
        self.name = new_name
        self.email = new_email
        print(f"User has been updated to '{self.name}', email: '{self.email}'.")

    def delete_user(self):
        print(f"User '{self.name}' has been deleted.")
        self.name = None
        self.email = None


user = User("John Doe", "john@example.com")
user.create_user()
user.update_user("Jane Doe", "jane@example.com")
user.delete_user()

print("==============")
# Завдання 2: Принцип відкритості/закритості (OCP)

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

class AreaCalculator:
    @staticmethod
    def calculate(shape: Shape):
        return shape.calculate_area()


circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Circle area: {AreaCalculator.calculate(circle)}")
print(f"Rectangle area: {AreaCalculator.calculate(rectangle)}")

print("==============")
# Завдання 3: Принцип підстановки Лісков (LSP)

class RectangleLSP(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class SquareLSP(RectangleLSP):
    def __init__(self, side):
        super().__init__(side, side)


def print_area(shape: Shape):
    print(f"Area: {shape.calculate_area()}")


rectangle_lsp = RectangleLSP(4, 5)
square_lsp = SquareLSP(4)
print_area(rectangle_lsp)
print_area(square_lsp)

print("==============")
# Завдання 4: Принцип інтерфейсу користувача (ISP)

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class BasicPrinter(Printer):
    def print_document(self):
        print("Printing document...")

class AdvancedScanner(Scanner):
    def scan_document(self):
        print("Scanning document...")


printer = BasicPrinter()
printer.print_document()

scanner = AdvancedScanner()
scanner.scan_document()

print("==============")
# Завдання 5: Принцип залежностей (DIP)

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class UserNotifier:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def notify(self, message):
        self.notification_service.send(message)


email_notifier = UserNotifier(EmailNotification())
email_notifier.notify("Hello via Email!")

sms_notifier = UserNotifier(SMSNotification())
sms_notifier.notify("Hello via SMS!")
