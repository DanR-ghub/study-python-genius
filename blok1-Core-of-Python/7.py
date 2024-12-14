#Наслідування

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        return f"Двигун автомобіля {self.make} {self.model} запущено!"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def do_wheelie(self):
        return f"Мотоцикл {self.make} {self.model} робить віли!"

class Bicycle(Vehicle):
    def __init__(self, make, model, year, is_electric):
        super().__init__(make, model, year)
        self.is_electric = is_electric

    def ring_bell(self):
        return f"Велосипед {self.make} {self.model} дзвонить у дзвіночок!"

car = Car("Toyota", "Corolla", 2022, "Бензин")
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, False)
bicycle = Bicycle("Giant", "Explore E+", 2023, True)

print(f"Автомобіль: {car.make}, {car.model}, {car.year}, {car.fuel_type}")
print(car.start_engine())
print(f"Мотоцикл: {motorcycle.make}, {motorcycle.model}, {motorcycle.year}, {'з коляскою' if motorcycle.has_sidecar else 'без коляски'}")
print(motorcycle.do_wheelie())
print(f"Велосипед: {bicycle.make}, {bicycle.model}, {bicycle.year}, {'електричний' if bicycle.is_electric else 'звичайний'}")
print(bicycle.ring_bell())
print("===================")
#Поліморфізм

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
            return f"Це {self.make} {self.model} {self.year} року виробництва."

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        return f"Автомобіль {self.make} {self.model}, {self.year} року, працює на {self.fuel_type}."

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        return f"Мотоцикл {self.make} {self.model}, {self.year} року, {'з коляскою' if self.has_sidecar else 'без коляски'}."

class Bicycle(Vehicle):
    def __init__(self, make, model, year, is_electric):
        super().__init__(make, model, year)
        self.is_electric = is_electric

    def display_info(self):
        return f"Велосипед {self.make} {self.model}, {self.year} року, {'електричний' if self.is_electric else 'звичайний'}."

vehicles = [
    Car("Toyota", "Corolla", 2022, "Бензин"),
    Motorcycle("Harley-Davidson", "Street 750", 2019, False),
    Bicycle("Giant", "Explore E+", 2023, True)
]

for vehicle in vehicles:
    print(vehicle.display_info())
