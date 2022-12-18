x = 0

def setup():
    size(600,400)
def draw():
    global x
    y = 0
    
    while y < height:
        fill(random(100,250),random(100,250) ,random(100,250))
        rect(x,y,30,2)
        y = y + 2
    x = x + 3
    if x > width:
        noLoop()
