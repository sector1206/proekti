x = 0
y = 0
z = -4
c = -5
e = -5
i = -4
o = -5
p = 54
d = 54
f = -5
h = -5
def setup():
  background(255)
  size(1500,300)
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
        translate(0,249)
        push()
        noStroke()
        rect(z,c,-5,59)
        rect(z,i,59,-5)
        rect(o,p,59,6)
        rect(d,f,6,59)
        pop()
        rect(x,y,50,50)
        pop()
        push()
       # frameRate(5)
        ellipse(random(300,900),random(50,250),random(25,45),random(25,45))
        pop()
