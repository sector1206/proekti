x = 0
y = 50
def setup():
  size(600,400)
def draw():
  global x
  global y
  background(100)
  fill(random(0,255),random(0,255),random(0,255))
  ellipse(x,350,50,50)
  ellipse(x,300,50,50)
  ellipse(x,250,50,50)
  ellipse(x,50,50,50)
  ellipse(x,100,50,50)
  ellipse(x,150,50,50)
  ellipse(x,400,50,50)
  ellipse(x,200,50,50)
  ellipse(x,0,50,50)
  ellipse(y,350,50,50)
  ellipse(y,300,50,50)
  ellipse(y,250,50,50)
  ellipse(y,50,50,50)
  ellipse(y,100,50,50)
  ellipse(y,150,50,50)
  ellipse(y,400,50,50)
  ellipse(y,200,50,50)
  ellipse(y,0,50,50)
  x = x + 10
  y = y + 10
  if x >= 600:
      if y >= 600:
          x = 0
          y = 50
