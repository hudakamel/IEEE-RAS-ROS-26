def analyze_grades():
    numbers_input = input("Enter the numbers: ").split()

    numbers = []
    for num in numbers_input:
        numbers.append(int(num))

    total = 0
    for num in numbers:
        total += num

    average = total / len(numbers)

    result = {
        "average": average,
        "highest": max(numbers),
        "lowest": min(numbers)
    }

    return result


print(analyze_grades())