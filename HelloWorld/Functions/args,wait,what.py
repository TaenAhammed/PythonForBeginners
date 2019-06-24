# *args, wait, what?


def increment(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(increment(1, 2, 3, 4))
