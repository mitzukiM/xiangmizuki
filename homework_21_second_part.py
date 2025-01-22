def multiply(*args):
    total = 1
    for some_number in args:
        total *= some_number
    return total


print(multiply(2, 3, 4))
