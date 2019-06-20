# Perform a task
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to the class")


# greet_user('Taen', 'Ahammed')

# Keyword arguments
greet_user(last_name='Taen', first_name='Ahammed')
greet_user('Tarif', last_name='Ahammed')


# Return a values
def greet(first_name, last_name):
    return f"Hi {first_name} {last_name}"


message = greet("Taen", "Ahammed")
file = open('./HelloWorld/Functions/content.txt', 'w')
file.write(message)
file.close()
