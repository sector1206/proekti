x = 0
def setup():
    size(800,600)
def draw():
    global x
    background(100)
    rect(0,0,x,x)
    if mouseButton == (LEFT):
        x= x + 1

       
