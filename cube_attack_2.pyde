x = 0
y = 0
z = -5
c = -5
e = -5
i = -5
o = -5
p = 55
d = 55
f = -5
h = 80
def setup():
  background(200)
  size(600,400)
def draw():
    #игрок, начало создания
    global x,y,z,c,e,i,o,p,d,f,h
    if keyPressed:
        if key == 'a':
            x = x - 5
        if key == 'w':
            y = y - 5
        if key == 'd':
            x = x + 5
        if key == 's':
            y = y + 5
        if key == 'a':
            z = z - 5
        if key == 'w':
            c = c - 5
        if key == 'd':
            z = z + 5
        if key == 's':
            c = c + 5
        if key == 'a':
            e = e - 5
        if key == 'w':
            i = i - 5
        if key == 'd':
            e = e + 5
        if key == 's':
            i = i + 5
        if key == 'a':
            o = o - 5
        if key == 'w':
            p = p - 5
        if key == 'd':
            o = o + 5
        if key == 's':
            p = p + 5
        if key == 'a':
            d = d - 5
        if key == 'w':
            f = f - 5
        if key == 'd':
            d = d + 5
        if key == 's':
            f = f + 5
        
        push()
        noStroke()
        rect(z,c,1,57)
        rect(e,i,57,1)
        rect(o,p,57,1)
        rect(d,f,1,57)
        rect(h,y,-6,1)
        pop()
        rect(x,y,50,50)
