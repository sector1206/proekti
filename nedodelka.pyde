x = 60
y = 1
c = 60
def setup():
  size(1000,1000)
  background(255)
def draw():
  global x,y,c
  stroke(0,255,0)
  strokeWeight(c)

  for y in range(1,7+1): # повторение строки
      for x in range(1,10+1):  #строка
          point(x*60,y*60) # элемент строки
  if y == 1:
      c = c + 1
  if y == -1:
      c = c - 1
  if c >= 70:
      y = -1
  if c <= 50:
      y = 1
