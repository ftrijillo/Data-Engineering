def fibonacci(n):
    fib_series = [0, 1]
    # first two terms
    n1, n2 = 0, 1

    # check if the number of terms is valid
    if n <= 0:
        return []
    # if there is only one term, return n1
    elif n == 1:
        return fib_series

    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while n2 < n:
            nth = n1 + n2
            if nth > n:
                break
            fib_series.append(nth)

            # update values
            n1 = n2
            n2 = nth

    return fib_series


print(fibonacci(1))
