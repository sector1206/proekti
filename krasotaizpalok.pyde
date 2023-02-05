x = 2
y = 0
c = 2
v = 0
def setup():
    size(1000,1000)
    background(150)
def draw():
    global x,y,c,v
    frameRate(15)
    push()
    translate(height/2,width/2)
    strokeWeight(1)
    rotate(x)
    noFill()
    ellipse(2,0,400,700)
    x = x - 0.1
    y = y + 0.1
    pop()
    push()
    translate(height/2,width/2)
    strokeWeight(1)
    rotate(c)
    noFill()
    ellipse(2,0,400,700)
    c = c + 0.1
    v = v + 0.1
    pop()
    push()
    translate(height/2,width/2)
    strokeWeight(1)
    rotate(c)
    noFill()
    ellipse(2,0,160,280)
    c = c + 0.1
    v = v + 0.1
    pop()
    push()
    translate(height/2,width/2)
    strokeWeight(1)
    rotate(x)
    noFill()
    ellipse(2,0,160,280)
    x = x - 0.1
    y = y + 0.1
    pop()
    
