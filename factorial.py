def factorial(n):
    result = 1  # something we will add to
    for num in range(2, n + 1):
        result *= num
    return result


print(factorial(5))
