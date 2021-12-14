# -*- 생성자와 소멸자 -*-
class MyClass:
    # constructor method (responsible for initialization)
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    # destructor method (executed the last)
    def __del__(self):
        print("Instance is deleted!")

# generating an instance
d = MyClass(5)

# memory management is automatic
# del d

print("[+] exited all code executions")

# garbage collector is executed periodically.

