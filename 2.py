def factorial(n):
    if n==0:
        return 1
    return multiply(n, factorial(n-1))


def multiply(x,y):
    if x==0:
        return 0

    return multiply(x-1, y) + y
