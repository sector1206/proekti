def draw():
    if keyPressed:
        if key == '3':
            fill(random(50,255),0,0)
        if key == '2':
            fill(0,random(0,255),0)
        if key == '1':
            fill(0,0,random(0,255))
    else:
        fill(255)

    rect(25, 25, 50, 50)
