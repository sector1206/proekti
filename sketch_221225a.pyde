x = -1
y = 650
def setup():
    size(600,400)
def draw():
    global x,y
   
    background(200)
    ellipse(x,300,50,50)
    ellipse(y,200,50,50)
    if x <= 650:
        x = x + 8
    if x >= 650:
        y = y - 8
    if y <= -30:
        x = x + 8
        x = -1
    ellipse(300,175,80,80)
    ellipse(300,135,50,50)
    ellipse(300,100,30,30)
    line(290,100,296,104)
    line(296,104,303,104)
    line(303,104,309,100)
    ellipse(295,95,5,5)
    ellipse(305,95,5,5)
    push()
    fill(139,69,19)
    rect(100,200,25,80)
    fill(0,200,0)
    triangle(50,200,112.5,150,180,200)
    triangle(60,150,112.5,110,170,150)
    triangle(70,110,112.5,80,160,110)
    translate(400,0)
    fill(139,69,19)
    rect(100,200,25,80)
    fill(0,200,0)
    triangle(50,200,112.5,150,180,200)
    triangle(60,150,112.5,110,170,150)
    triangle(70,110,112.5,80,160,110)
    pop()
    
