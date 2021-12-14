# class1.py

class Person:
    # initial method
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))


# generating an instance
p1 = Person()
p1.print()

