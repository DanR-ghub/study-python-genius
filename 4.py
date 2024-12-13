# ------ Робота із списками ------
numbers = [1, 2, 3, 4, 5]
numbers.append(10)
numbers.append(20)
numbers.remove(10)
print("Робота із списками:", numbers)

# ------ Знаходження суми ------

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("Знаходження суми:", total)

# ------ Подвійні значення ------

numbers = [1, 2, 3, 4, 5]
for x in range(len(numbers)):
    numbers[x]=numbers[x]*2
print("Подвійні значення:", numbers)

# ------ Робота із кортежами ------

fruits = ("яблуко", "банан", "апельсин")
print("Робота із кортежами:")
for i in fruits:
    print(i)

# ------ Об'єднання кортежів ------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Об'єднання кортежів:", combined_tuple)

# ------ Робота із словниками ------

athlete = {
    "ім'я": "Лео",
    "вік": 36,
    "спорт": "футбол",
    "команда": "Якась"
}
print("Робота із словниками:", athlete)

# ------ Оновлення словника ------

books = {
    "Гаррі Поттер": 1997,
    "Лялька": 1879
}
books["1984"] = 1949
print("Оновлення словника:", books)

# ------ Пошук значення ------

capitals = {
    "Україна": "Київ",
    "Франція": "Париж",
    "Польща": "Варшава"
}
country = input("Введіть назву країни: ")
capital = capitals.get(country)
if capital:
    print(f"Столиця {country}: {capital}")
else:
    print("Такої країни немає у словнику.")
