# DemoTimeDate.py

# import time

# print(time.time())

# print( dir(time))

# print(time.process_time())
# print(time.process_time_ns())

# print("--- gmtime ---")
# print(time.gmtime())
# mytime = time.gmtime()
# print(dir(mytime))
# print(mytime.tm_hour)
# print(mytime.tm_min)
# print(mytime.tm_sec)

# print("--- localtime ---")
# print(time.localtime())
# mylocaltime = time.localtime()
# print(mylocaltime.tm_hour)
# print(mylocaltime.tm_min)
# print(mylocaltime.tm_sec)

from datetime import *

d1 = date(2021, 12, 25)
print(d1)
print(dir(d1))

d2 = date.today()
d3 = timedelta(days=100)
print(d2+d3)


# 파일이름
print("c:\\work\\test.txt")
print("c:\\work\\newfile.txt")

print(r"c:\work\test.txt")
print(r"c:\work\newfile.txt")

from os.path import *
# print(dir())
print(abspath("python.exe"))
print(basename("c:\\python38\\python.exe"))
print( getsize("c:\\python38\\python.exe"))
print(exists("c:\\python38\\python.exe"))

from os import *

print("운영체제이름:", name)
# system("notepad.exe")


import random

print(random.random())
print(random.random())

print(random.sample(range(10), 10))
print(random.sample(range(10), 10))
print(random.sample(range(10), 10))
print(random.sample(range(10), 10))

# 로또번호 생성
lotto = list(range(1, 46))
print(lotto)
random.shuffle(lotto)
print(lotto)
lotto = lotto[0:6]
lotto.sort()
print(lotto)


import glob
result = glob.glob("c:\\work\\*.py")
#print(result)
for item in result:
    print(basename(item))