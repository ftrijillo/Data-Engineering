def sum_of_digits(num: int):
    numbers = [int(x) for x in str(num)]
    return sum(numbers)


print(sum_of_digits(5585))
