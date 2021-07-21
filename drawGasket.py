import math,turtle
def darwGasket(pen,size):
    if size < 10 :
        return
    for i in range(3):
        pen.fd(size/2)
        insertGasket(pen,size)
        pen.fd(size/2)
        pen.right(120)
def insertGasket(pen,size):
    pen.lt(120)
    darwGasket(pen,size/2)
    pen.rt(120)
def oneSide(pen,s,diag,level):
    if (level==0):
        return
    else:
        oneSide(pen,s,diag,level-1)
        pen.rt(45);pen.fd(diag);pen.rt(45)
        oneSide(pen,s,diag,level-1)
        pen.rt(90);pen.fd(s);pen.rt(90)
        oneSide(pen,s,diag,level-1)
        pen.rt(45);pen.fd(diag);pen.rt(45)

def curve(pen,s,level):
    diag=s/math.sqrt(2)
    for i in range(4):
        oneSide(pen,s,diag,level)
        pen.rt(45)
        pen.fd(diag)
        pen.rt(45)
def main():
    turtle.title("recursive figures")
    turtle.setup(1000,1000,0,0)
    pen=turtle.Turtle()
    pen.speed(0)
    # curve(pen,15,3)
    #
    #
    darwGasket(pen,200)
    
    turtle.done()
main()