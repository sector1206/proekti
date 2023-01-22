z = 0
x = -300
c = -600
def setup():
    size(1000,1000)
def draw():
    background(0,0,255)
    global z,x,c
    fill(0,255,0)
    rect(-2,800,1004,250)
    img = loadImage("hfrtnf.jpg")
    image(img,z,750,250,250)
    img = loadImage("hfrtnf.jpg")
    image(img,x,750,250,250)
    img = loadImage("hfrtnf.jpg")
    image(img,c,750,250,250)
    img = loadImage("tankuy.jpg")
    image(img,0,750,250,250)
    fill(255,255,0)
    ellipse(800,200,200,200)
    z = z + 4
    x = x + 4
    c = c + 4
    if z >= 1300:
        z = 0
    if x >= 1300:
        x = 0
    if c >= 1300:
        c = 0
    
