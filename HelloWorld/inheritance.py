# Inheritance is a machanism for reusing code.


class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    # pass
    def bark(self):
        print("Bark")


class Cat(Mammal):
    # pass
    def be_annoying(self):
        print("Be Annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoying()
