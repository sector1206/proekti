x = 100
y = 255
c = 20
q = 275
w = 325
i = 0
def setup():
    size(600,400)
def draw():
    global x,y,c,q,w,i
    fill(255,y,y)
    ellipse(300,200,x,x)
    push()
    strokeWeight(i)
    line(275,215,325,215)
    pop()
    ellipse(q,175,c,c)
    ellipse(w,175,c,c)
    x = x + 3
    y = y - 1
    c = c + 2
    q = q - 1.5
    w = w + 1.5
    i = i + 0.25
    
