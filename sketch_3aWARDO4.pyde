x = -600
y = 1000
def setup():
    size(2000,1000)
def draw():
    global y,x
    background(0)
    img = loadImage("pl.jpg")
    image(img, 200, 200)
    img = loadImage("sun5.jpg")
    image(img, 1000, -1500,4000,4000)
    img = loadImage("asasas.png")
    image(img,y,x,200,200)
    y = y - 16
    x = x + 32
    if y <= 500:
        x = -1000
        y = 4000
