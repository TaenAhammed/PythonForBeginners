names = ['John', 'Bob', 'Mosh', 'Sarah', 'Marry']
print(names[2])
print(names[-1])
print(names[-3])

print(names[2:])
print(names[:])
print(names[1:4])
names[0] = 'Jon'
print(names)

# Exercise

numbers = [23, 343, 54, 23, 4, 500, 43]

largest_num = numbers[0]

for number in numbers:
    if largest_num < number:
        largest_num = number
print(largest_num)
