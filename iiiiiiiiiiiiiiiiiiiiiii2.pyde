x = 400
y = -1000
c = -1000
def setup():
    size(1000,900)
def draw():
    background(200)
    global x,y,c
    img = loadImage("iii.jpg")
    image(img,200,200,200,200)
    img = loadImage("CTRASHNO.jpg")
    image(img,x,200,200,200)
    c = c - 5
    x = x - 10
    if x <= 200:
        x = -1000  
        y = 200  
        img = loadImage("ooo.jpg")
        image(img,y,200,200,200)
    if y >= 200:
        img = loadImage("ppp.jpg")
        image(img,c,200,200,200)
        c = 600
