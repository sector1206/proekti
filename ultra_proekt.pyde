x = 0
y = 200
b = 0
c = 0
v = 0
n = 870
m = 0
a = 255
s = 255
d = 255
def setup():
    size(1200,900)
def draw():
    global x,c,v,b,y,n,a,s,d,m
    background(b,c,v)
    push()
    translate(600,900)
    rotate(radians(x))
    fill(255,255,0)
    ellipse(-600,200,150,150)
    fill(200,200,200)
    ellipse(600,-200,80,80)
    ellipse(y,200,1,1)
    pop()
    push()
    noStroke()
    fill(139, 69, 19)
    rect(300,600,50,250)
    fill(139, 69, 19)
    rect(700,600,50,250)
    fill(a,s,d)
    ellipse(325,600,200,200)
    ellipse(725,600,200,200)
    ellipse(200,n,500,100)
    ellipse(400,n,500,100)
    ellipse(600,n,500,100)
    ellipse(800,n,500,100)
    ellipse(1000,n,500,100)
    pop()
    y = y + 1
    x = x + 1
    m = m + 1
    if y <= 380:
        b = b + 1
        c = c + 1
        v = v + 2
    if y >= 380:
        b = b - 1
        c = c - 1
        v = v - 2
    if y >= 560:
        y = 200
    if  m <= 10:
        n = n + 1
    if m <= 102:
        a = a - 2.5
        d = d - 2.5
        
