size(1000,1000)
background(255)
stroke(0,255,0)
strokeWeight(3)

y = 1 # 
for y in range(1,250+1): # повторение строки
    for x in range(1,300+1):  #строка
        rect(x*5,y*5,x*5,y*5) # элемент строки
