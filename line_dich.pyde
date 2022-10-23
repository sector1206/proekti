x = 1000
y = 1000
def setup():
  size(600,400)
  background(200)
def draw():
  global x
  global y
  line(x,y,600,400)
  x = x - 3
  y = y - 3
