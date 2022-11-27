y = 0
x = 0
def setup():
  size(1000,1000)
  background(255)
def draw():
  fill(0)  
  #ackground(255)
def keyPressed():
    ellipse(x,y,50,50)
    global x
    global y
    if key == CODED:
        if keyCode == UP:
            y = y - 5
        if keyCode == RIGHT:
            x = x + 5
        if keyCode == DOWN:
            y = y + 5
        if keyCode == LEFT:
            x = x - 5
    else:
        fill(255)
        
        
        
        
         
    
