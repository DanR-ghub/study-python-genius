import calculator

def main():
    print("Калькулятор:")
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = input("Введіть операцію (+, -, *, /): ")

    if operation == "+":
        result = calculator.add(a, b)
    elif operation == "-":
        result = calculator.subtract(a, b)
    elif operation == "*":
        result = calculator.multiply(a, b)
    elif operation == "/":
        result = calculator.divide(a, b)
    else:
        print("Невідома операція!")
        return

    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
