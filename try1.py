# try1.py
# definition of function
def divide(a, b):
    return a/b

# error handling (화면단에서 처리)
try:
# call
    result = divide(5, 2)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
except TypeError:
    print("문자로 나누면 안됩니다")
else:
    print("결과: {0}".format(result))
finally:
    print("한번 더 체크(무조건 실행")


print("전체 코드 실행 종료")

