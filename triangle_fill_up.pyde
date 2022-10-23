x = 0
def setup():
  size(600,400)
  background(200)
def draw():
  global x
  fill(x,x,x)
  noStroke()
  triangle(200,200,300,100,400,200)
  x = x + 1
