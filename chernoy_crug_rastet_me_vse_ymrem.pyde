x = 0
def setup():
    size(600,400)
def draw():
    background(255)
    global x
    fill(0)
    ellipse(300,200,x,x)
    if keyPressed:
        if key == 's':
            x = x - 5
        if key == 'b':
            x = x + 5

    else:
        fill(255)
        
        
