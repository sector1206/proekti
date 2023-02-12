size(800,600)
background(255)
stroke(0,255,0)
strokeWeight(90)

y = 1 # 
push()
for y in range(1,7+1):
    translate(60,0)
    point(60,60*y)
pop()
for x in range(1,7+1):
    translate(0,-60)
    point(60*x,480)
