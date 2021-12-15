# DemoFile.py

# 문자열 결합 연산
url = "http://www.credu.com/?page=" + str(1)
print(url)

# 위치 지정
for i in range(1,6):
    print(i, "*", i, "=", i*i)

for i in range(1,6):
    print(i, "*", i, "=", str(i*i).rjust(3))

for i in range(1,6):
    print(i, "*", i, "=", str(i*i).zfill(3))


print("서식문자")
print("{0:x}".format(10))
print("0x{0:x}".format(10))
print("0x{0:X}".format(10))
print("0x{0:X}".format(1000000))
print("0x{0:08X}".format(1000000))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(150000000000000))


print("------ file I/O -------")
print("------ write -------")
# 파일을 쓰기 (인코딩->유니코드)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

print("------ read -------")
f = open("c:/work/demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)

print(f.tell())
f.seek(0)

print(f.readline(), end="")
print(f.readline(), end="")

f.seek(0)
lst = f.readlines()
print(lst)



