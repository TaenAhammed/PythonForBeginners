course = 'Python for Beginners'
print(len(course))  # Genereal perpous function
print(course.upper())
print(course)
print(course.lower())

# Returns the index of the first occurrence of the character.
print(course.find('P'))
print(course.find('B'))
print(course.find('o'))
print(course.find('O'))
print(course.find('Beginners'))

print(course.replace("Beginners", "Absolute Beginners"))
print(course.replace("P", "C"))

# Check existence of a character or a sequence of characters
print("Python" in course)   # True
print("python" in course)   # False
