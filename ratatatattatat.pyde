def setup():
  size(1000,1000)
  background(255)
  stroke(0,255,0)
  strokeWeight(3)
def draw():
    frameRate(1000)
    y = 1 
    for y in range(1,250+1): # повторение строки
        for x in range(1,300+1):  #строка
            fill(random(0,255))
            rect(x*30,y*30,x*30,y*30) # элемент строки
