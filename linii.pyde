x = 2
y = 0
def setup():
    size(1000,1000)
    background(150)
def draw():
    global x,y
    translate(height/2,width/2)
    rotate(x)
    strokeWeight(10)
    stroke(random(0,255),random(0,255),random(0,255))
    line(2,0,500,500)
    x = x - 0.1
    y = y + 0.1
        
