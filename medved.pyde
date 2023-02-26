x = 301
y = 5
def setup():
    size(800,800)
def draw():
    background(180)
    global x,y
    ellipse(400,400,500,700)
    ellipse(250,650,100,100)
    ellipse(550,650,100,100)
    push()
    translate(170,300)
    rotate(radians(25))
    ellipse(0,0,80,150)
    pop()
    ellipse(650,x,80,201)
    x = x + y
    if x <= 300 or x >= 500:
        y = -y
