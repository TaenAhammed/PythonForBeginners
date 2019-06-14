class Point:
    # constructor function
    def __init__(self, x, y):       # self references to the current object
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.move()
print(point.x)
point.x = 11
print(point.x)

# exercise


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I'm {self.name}.")


taen = Person("Taen Ahammed")
taen.talk()

tarif = Person('Tarif Ahmed')
print(tarif.name)
tarif.talk()
