x = 0
def setup():
    size(1000,1000)
def draw():
    frameRate(400)
    global x
    background(255)
    translate(500,500)
    rotate(radians(x))
    img = loadImage("ultra_trio.jpg")
    image(img,-500,-500,1000,1000)
    x = x + 1.5
