y = 0

def setup():
    size(600,400)
def draw():
    global y
    x = 0
    
    while x < width:
        fill(random(100,250),random(100,250) ,random(100,250))
        rect(x,mouseY,30,30)
        x = x + 30
    if y > height:
        noLoop()
