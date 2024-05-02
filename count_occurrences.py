def count_occurrences(numbers, target):
    occurrence = 0

    if len(numbers) >= 0:
        for i in numbers:
            if i == target:
                occurrence += 1

    return occurrence


print(count_occurrences([1, 2, 5, 3, 4, 2, 2, 5], 5))
