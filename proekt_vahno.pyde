x = 100
y = 300
def setup():
    size(800,600)
def draw():
    background(100,100,255)
    global x,y
    ellipse(x,y,75,75)
    push()
    translate(200,425)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    triangle(0,0,40,-75,80,0)
    translate(80,0)
    pop()
    push()
    translate(200,175)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    triangle(0,0,40,75,80,0)
    translate(80,0)
    pop()
    frameRate(10)
    y = y + 3
    x = x + 9
    if y >= 375:
        push()
        textSize(80)
        fill(0)
        textAlign(CENTER,CENTER)
        text(u"ты проиграл",300,300)
        pop()
        x = 100
def mousePressed():
    if mouseButton == LEFT:
        global x,y
        y = y - 3