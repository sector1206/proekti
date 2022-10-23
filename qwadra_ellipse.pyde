x = 300
y = 200
q = 300
w = 200
e = 300
r = 200
t = 300
u = 200
def setup():
  size(600,400)
  background(0)
def draw():
  global x
  global y
  global q
  global w
  global e
  global r
  global t
  global u
  ellipse(x, y, 50,50)
  ellipse(q, w, 50,50)
  ellipse(e, r, 50,50)
  ellipse(t, u, 50,50)
  x = x + 1
  y = y + 1
  q = q + 1
  w = w - 1
  e = e - 1
  r = r - 1
  t = t - 1
  u = u + 1
