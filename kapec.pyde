x = 900
def setup():
  size(600,400)
def draw():
  global x
  background(100)
  fill(random(0,255),random(0,255),random(0,255))
  translate(300,200)
  ellipse(0,0,x,x)
  x = x - 2
  if x <= 0:
      noLoop()
