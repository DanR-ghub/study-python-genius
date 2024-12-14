def calculate_avg(numbers):
    if not numbers:
        return "Список порожній!"
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if not numbers:
        return "Список порожній!"
    return max(numbers)
