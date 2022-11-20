x = 50
y = 50
def setup():
    size(1000,1000)
def draw():
    background(255)
    global x
    global y
    fill(0)
    rect(x,y,50,50)
    if keyPressed:
        if keyCode == RIGHT:
            x = x + 3
    if keyPressed:
        if keyCode == DOWN:
            y = y + 3
    if keyPressed:
        if keyCode == LEFT:        
            x = x - 3
    if keyPressed:
        if keyCode == UP:
            y = y - 3        
