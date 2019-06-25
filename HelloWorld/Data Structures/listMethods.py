numbers = [5, 2, 1, 5, 7, 4]

# numbers.append(20)
# numbers.insert(0, 10)
# numbers.remove(5)
# numbers.clear()
# numbers.pop()


# print(numbers.index(50))
print(5 in numbers)
print(50 in numbers)

print(numbers.count(5))

numbers.sort()
numbers.reverse()

numbers2 = numbers.copy()
numbers.append(10)
numbers.append(100)

print(numbers)
print(numbers2)

# Exercise -> Remove duplicates in a list
numbers = [1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 9]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
