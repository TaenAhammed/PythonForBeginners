try:
    age = int(input("Age: "))
    income = 1000
    risk = income / age
    print(age)

except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print("You entered invalid value!!!")
