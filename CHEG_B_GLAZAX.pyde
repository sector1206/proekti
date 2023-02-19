x = 10
y = 10
def setup():
    size(600,400)
    background(20)
def draw():
    global x,y
    ellipse(random(0,600),random(0,200),x,y)
    x = x + 3
    y = y + 3
    
