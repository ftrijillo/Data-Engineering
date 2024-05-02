def calculate_average(numbers):

    if len(numbers) <= 0:
        return 0

    tot = 0
    for i in numbers:
        tot += i

    average = tot / len(numbers)

    return average


print(calculate_average([5, 10, 15, 20]))
