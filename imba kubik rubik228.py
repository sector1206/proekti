import random
e= random.randint(0, 10)
q = int(input("выбери число"))
if q > e:
    print("загаданное число меньше")
if q < e:
    print("загаданное число больше")
    if q == e:
        print("угадал")
        print(e)
w = int(input("выбери число"))
if w > e:
    print("загаданное число меньше")
if w < e:
    print("загаданное число больше")
    if w == e:
        print("угадал")
        print(e)
a = int(input("выбери число"))
if a > e:
    print("загаданное число меньше")
if a < e:
    print("загаданное число больше")
    

if a == e:
    print("угадал")

print(e)
