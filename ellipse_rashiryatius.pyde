x = 1000
def setup():
  size(600,400)
  background(0)
def draw():
  global x
  ellipse(300,200,x,x)
  x = x - 3
