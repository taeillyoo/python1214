# Function2.py

# 불변형식과 가변형식

print("---immutable---")
a = 1.2
print(id(a))
a = 2.3
print(id(a))

print("---mutable---")
lst = [1, 2, 3]
print(lst)
print(id(lst))
lst.append(lst)
print(lst)
print(id(lst))


# LGB scoping rule
x = 2

# definition of function
def func1(a):
    return a + x

# calling
print(func1(1))


def func2(a):
    x = 5
    return a+x


print(func2(1))


# basic value
def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5, 6))


# keyword parameters
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

# call
print(connectURI("credu.com", "80"))
print(connectURI(port="80", server="credu.com"))

# variadic arguments
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# call
print( union("HAM", "SPAM"))
print( union("HAM", "SPAM", "EGG"))



# undefined arguments
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

# calling
print(userURIBuilder("credu.com", "80", id="kim", name="mike"))
print(userURIBuilder("credu.com", "80", id="kim", name="mike", 
    age = "30"))

