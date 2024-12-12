# 1. Перевірка паролю -------------------------------------------

users = {
    "user1": {"name": "Іван", "password": "password123"},
    "user2": {"name": "Марія", "password": "12345"}
}

username = "user1"
user_password = "password123"

if users.get(username, {}).get("password") == user_password:
    print(f"Ви увійшли в систему як {users[username]['name']}")
else:
    print("Неправильний пароль")

# 2. Визначення днів тижня -------------------------------------

days_of_week = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П'ятниця",
    6: "Субота",
    7: "Неділя"
}

day_number = int(input("Введіть номер дня тижня (1-7): "))

if day_number < 1 or day_number > 7:
    raise ValueError("Невірний номер дня тижня")
else:
    print(days_of_week[day_number])
    
# 3. Таблиця множення -------------------------------------------

multiplication_table = {}

number = 5

for i in range(1, 11):
    multiplication_table[i] = number * i

for i, result in multiplication_table.items():
    print(f"{number} x {i} = {result}")

# 4. Сума чисел ------------------------------------------------

numbers = {
    "num1": 3,
    "num2": 5,
    "num3": 7,
    "num4": 10,
    "num5": 15
}

total_sum = sum(numbers.values())

print("Сума чисел:", total_sum)

# 5. Факторіал числа -------------------------------------------

factorials = {}

n = 5

factorial = 1
for i in range(1, n + 1):
    factorial *= i

factorials[n] = factorial

print(f"Факторіал числа {n} = {factorials[n]}")

# 6. Парні числа -----------------------------------------------

even_numbers = {}

for i in range(1, 51):
    if i % 2 == 0:
        even_numbers[f"even_{i}"] = i

for key, value in even_numbers.items():
    print(value)

# 7. Пошук простих чисел ---------------------------------------

prime_numbers = {}

start = 1
end = 50

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers[f"prime_{num}"] = num

for key, value in prime_numbers.items():
    print(value)
