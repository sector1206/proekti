x = 2
y = 0
def setup():
    size(1000,1000)
    background(150)
def draw():
    global x,y
    translate(height/2,width/2)
    rotate(x)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(x,y,100,100)
    x = x - 0.5
    y = y + 0.5
        
