numbers = [1, 2, 3]

# List unpacking
x, y, z = numbers
print(x, y, z)

numbers = (1, 2, 3)
x, y, z = numbers
print(x, y, z)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
first, second, *others, second_last, last = numbers
print(first, second, second_last, last)
print(others)
