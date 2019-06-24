# *args, wait, what?


def increment(*numbers):
    # tuple
    print(numbers)

    total = 0
    for number in numbers:
        total += number
    return total


print(increment(1, 2, 3, 4))

# **args


def save_user(**user):
    # dictionary
    print(user)

    print(user['name'])


save_user(id=1, name='Taen Ahammed', age=20)
