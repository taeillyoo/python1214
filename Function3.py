# Function3.py

result = list(range(1,11))
print(result)

# generating years
years = list(range(2000, 2022))
print(years)

# minus -1
numbers = list(range(10, 0, -1))
print(numbers)

# list comprehension
lst = list(range(1,11))
result = [i**2 for i in lst if i>5]
print(result)

# filtering function
def getBiggerThan20(i):
    return i>20

# printing
lst = [10, 25, 30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)


print("--- lambda function ---")
iterL = filter(lambda x: x>20, lst)
for item in iterL:
    print(item)
