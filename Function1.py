# Function.py

# 함수 정의
def times(a, b):
    return a*b

# 호출
print( times(3,4) )

# 함수 정의
def setValue(newValue):
    x = newValue
    print(x)

# 호출
result = setValue(5)
print(result)

# 교집합 리스트를 리턴하는 함수
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출
print("---string---")
print( intersect("HAM", "SPAM"))
# print("---set---")
# print( intersect({"H", "A", "M"}, {"S", "P", "A", "M"}))


