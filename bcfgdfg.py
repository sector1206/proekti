a = 0

while a != 14:
    z = int(input("введи 1 чтобы отнять 1,введи 2 чтобы прибавить 2"))
    if z == 1:
        print("камешков теперь",a - 1)
        a -= 1
    if z == 2:
        print("камешков теперь",a+2)
        a += 2

