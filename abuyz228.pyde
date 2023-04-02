def setup():
    size(1000,800)
    background(200)
    strokeWeight(5)
def draw():
    if mousePressed and mouseButton == LEFT:
        line(mouseX,mouseY,mouseX,mouseY)
    elif mousePressed and mouseButton == RIGHT:
        background(200)
