def find_max_number(numbers):
    if numbers:
        s_numbers = list(numbers)
        s_numbers.sort()
        return s_numbers[-1]
    else:
        return None


print(find_max_number([5, 9, 2, 12, 7]))
