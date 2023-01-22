x = 0
y = 300
c = 500
v = 250
b = 250
def setup():
    size(1000,1000)
def draw():
     background(255)
     global y,c,v,b,x
     img = loadImage("lox.jpg")
     image(img,y,c,v,b)
     img = loadImage("maso.jpg")
     image(img,300,x,250,250)
     y = y - 1
     c = c - 1
     v = v + 2
     b = b + 2
     x = x + 10
     if x >= 500:
         x = 0
