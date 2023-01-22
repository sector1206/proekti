x = 0
c = 0
def setup():
    size(1000,1000)
def draw():
     background(255)
     global x,c
     img = loadImage("vfibyf.jpg")
     image(img,c,0,250,250)
     img = loadImage("vfibyf2.jpg")
     image(img,c,250,250,250)
     img = loadImage(";buekb.jpg")
     image(img,x,500,250,250)
     x = x + 2.5
     c = c + 2
     if x >= 750:
         c = 600
         x = 750
         textSize(60)
         fill(0)
         text(u"Победили жигули!", 300,800)

     
