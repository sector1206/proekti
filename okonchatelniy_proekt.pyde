x = 850
y = 874
c = 10
v = 25
a = 0
d = 30
h = -30
g = -30
b = -1
n = 0
m = 22
f = 6
q = 850
w = 874
e = 10
r = 25
t = 22
s = 6
i = 0
o = 0
p = -30
j = 30
k = -30
l = -1
def setup():
    size(1000,800)
    background(0)
def draw():
    textSize(30)
    fill(255)
    textAlign(CENTER,CENTER)
    text(u"с наступающим новым годом",700,700)
    global x,y,c,v,a,d,h,g,b,n,m,f,q,w,e,r,t,y,i,o,p,j,k,l,s
    push()
    fill(255,255,0)
    rect(500,x,c,v)
    pop()
    push()
    noStroke()
    fill(0)
    rect(500,y,m,f)
    pop()
    x = x - 5
    y = y - 5
    if x <=200:
        c = 0
        v = x
        a = a - 5
        d = d - 0
        h = h + 5
        m = 0
        f = 0
        #frameRate(1)
        push()
        translate(500,200)
        push()
        fill(200,183,20)
        rotate(radians(0))
        rect(n,a,10,30)
        pop()
        push()
        fill(200,183,20)
        rotate(radians(40))
        rect(n,a,10,30)
        pop()
        push()
        fill(200,183,20)
        rotate(radians(80))
        rect(n,a,10,30)
        pop()
        push()
        fill(200,183,20)
        rotate(radians(165))
        rect(n,h,10,30)
        pop()
        push()
        fill(200,183,20)
        rotate(radians(160))
        rect(n,a,10,30)
        pop()
        push()
        fill(200,183,20)
        rotate(radians(200))
        rect(n,a,10,30)
        pop()
        push()
        fill(200,183,20)
        rotate(radians(240))
        rect(n,a,10,30)
        pop()
        push()
        fill(200,183,20)
        rotate(radians(280))
        rect(n,a,10,30)
        push()
        fill(200,183,20)
        rotate(radians(320))
        rect(n,a,10,30)
        pop()
        push()
        fill(200,183,20)
        rotate(radians(0))
        rect(n,a,10,30)
        pop()
        pop()
        pop()
        if a <= -400:
            d = d - 5
            g = g + 5 
            push()
            translate(500,200)
            noStroke()
            fill(0)
            push()
            rotate(radians(0))
            rect(b,d,12,7)
            pop()
            push()
            rotate(radians(40))
            rect(b,d,12,7)
            pop()
            push()
            rotate(radians(80))
            rect(b,d,12,7)
            pop()
            push()
            rotate(radians(165))
            rect(b,g,12,7)
            pop()
            push()
            rotate(radians(160))
            rect(b,d,12,7)
            pop()
            push()
            rotate(radians(200))
            rect(b,d,12,7)
            pop()
            push()
            rotate(radians(240))
            rect(b,d,12,7)
            pop()
            push()
            rotate(radians(280))
            rect(b,d,12,7)
            pop()
            push()
            rotate(radians(320))
            rect(b,d,12,7)
            pop()
            pop()
            if x <= -2000:
                x = 850
                c = 10
                v = 25
                y = 874
                m = 22
                f = 6
                b = -1
                d = 30
                a = 0
                n = 0
                g = -30
                h = -30
            if x  <= 500:
                push()
                fill(55,255,55)
                rect(250,q,e,r)
                pop()
                push()
                noStroke()
                fill(0)
                rect(250,w,t,s)
                pop()
                q = q - 5
                w = w - 5
                if q <=200:
                    e = 0
                    r = q
                    i = i - 7
                    l = l - 0
                    p = p + 7
                    t = 0
                    s = 0
                    #frameRate(1)
                    push()
                    translate(250,200)
                    fill(100,255,100)
                    push()
                    rotate(radians(0))
                    rect(o,i,10,30)
                    pop()
                    push()
                    rotate(radians(40))
                    rect(o,i,10,30)
                    pop()
                    push()
                    rotate(radians(80))
                    rect(o,i,10,30)
                    pop()
                    push()
                    rotate(radians(165))
                    rect(o,p,10,30)
                    pop()
                    push()
                    rotate(radians(160))
                    rect(o,i,10,30)
                    pop()
                    push()
                    rotate(radians(200))
                    rect(o,i,10,30)
                    pop()
                    push()
                    rotate(radians(240))
                    rect(o,i,10,30)
                    pop()
                    push()
                    rotate(radians(280))
                    rect(o,i,10,30)
                    push()
                    rotate(radians(320))
                    rect(o,i,10,30)
                    pop()
                    pop()
                    pop()
                    if i <= -400:
                        j = j - 7 
                        k = k + 7
                        push()
                        translate(250,200)
                        noStroke()
                        fill(0)
                        push()
                        rotate(radians(0))
                        rect(l,j,12,7)
                        pop()
                        push()
                        rotate(radians(40))
                        rect(l,j,12,7)
                        pop()
                        push()
                        rotate(radians(80))
                        rect(l,j,12,7)
                        pop()
                        push()
                        rotate(radians(165))
                        rect(l,k,12,7)
                        pop()
                        push()
                        rotate(radians(160))
                        rect(l,j,12,7)
                        pop()
                        push()
                        rotate(radians(200))
                        rect(l,j,12,7)
                        pop()
                        push()
                        rotate(radians(240))
                        rect(l,j,12,7)
                        pop()
                        push()
                        rotate(radians(280))
                        rect(l,j,12,7)
                        pop()
                        push()
                        rotate(radians(320))
                        rect(l,j,12,7)
                        pop()
                        pop()
                        if q <= -1000:
                            q = 850
                            e = 10
                            r = 25
                            w = 874
                            t = 22
                            s = 6
                            l = -1
                            p = 30
                            i = 0
                            o = 0
                            p = -30
                            k = -30    
                            j = 30  
