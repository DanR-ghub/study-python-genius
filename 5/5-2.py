import utilities

def main():
    numbers = [10, 20, 30, 45, 50]
    print("Список чисел:", numbers)

    avg = utilities.calculate_avg(numbers)
    print(f"Середнє значення: {avg}")

    max_number = utilities.find_max(numbers)
    print(f"Максимальне число: {max_number}")

if __name__ == "__main__":
    main()
