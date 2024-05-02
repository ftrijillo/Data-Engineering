def find_closest_number(numbers, target):
    if len(numbers) == 0:
        return None

    numbers.sort()
    closest_num = numbers[0]
    for num in numbers:
        if abs(num - target) < abs(closest_num - target):
            closest_num = num
        if num > target:
            break
    return closest_num


print(find_closest_number([2, 4, 8, 10], 6))
