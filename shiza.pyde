angle = 0
angla = 0
x = 0
def setup():
  size(600,400)
def draw():
  global angle
  global x
  global angla
  push()
  translate(300,200)
  rotate(radians(angle))
  fill(random(0,255),random(0,255),random(0,255))
  ellipse(x,x,50,50)
  pop()
  translate(300,200)
  rotate(radians(angla))
  fill(random(0,255),random(0,255),random(0,255))
  ellipse(x,x,50,50)
  angla = angla - 1
  angle = angle + 1
  x = x + 0.1
  
