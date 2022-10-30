angle = 0
def setup():
  size(600,400)
def draw():
  global angle
  translate(300,200)
  rotate(radians(angle))
  fill(random(0,255),random(0,255),random(0,255))
  rect(-100,-100,100,100)
  angle = angle + 1
  
