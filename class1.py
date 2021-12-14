# class1.py

class Person:
    # initial method
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))


# generating an instance
p1 = Person()
p1.name = "second name"

p2 = Person()

p1.print()
p2.print()

# add a member in runtime
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

# add a member to the an instance
p1.age = 30
print(p1.age)
# print(p2.age)


