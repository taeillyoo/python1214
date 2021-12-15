# DemoStr.py

# print(dir(str))

# strA = "<<< python is very powerful  >>>"
# result = strA.strip("<> ")
# print(result)



# names = ["전우치", "이순신", "김길동"]
# for name in names:
#     print("안녕하세요. {0}님 추운 겨울입니다.".format(name))
#     print("=" * 40)


# 정규표현식: 특정한 패턴 검색
import re

result = re.match("[0-9]*th", "35th")
result2 = re.search("[0-9]*th", "35th")
print(result.group())
print(result2.group())


result = re.match("[0-9]*th", "  35th")
result2 = re.search("[0-9]*th", "  35th")
# print(result.group())
print(result)
print(result2.group())


result = re.search("apple", "this is apple")
print(result.group())

# 년도
result = re.search("\d{4}", "올해는 2021년입니다.")
print(result.group())

# 우편번호
result = re.search("\d{5}", "우리 동네는 51234입니다.")
print(result.group())

