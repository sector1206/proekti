x = 0
y = 200
b = 0
c = 0
v = 0
n
def setup():
    size(1200,900)
def draw():
    global x,c,v,b,y,n
    background(b,c,v)
    push()
    translate(600,900)
    rotate(radians(x))
    fill(255,255,0)
    ellipse(-600,200,150,150)
    fill(200,200,200)
    ellipse(600,-200,80,80)
    ellipse(y,200,1,1)
    pop()
    push()
    ellipse
    pop()
    y = y + 1
    x = x + 1
    if y <= 380:
        b = b + 1
        c = c + 1
        v = v + 2
    if y >= 380:
        b = b - 1
        c = c - 1
        v = v - 2
    if y >= 560:
        y = 200
