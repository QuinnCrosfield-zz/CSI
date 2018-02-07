import cTurtle
pi = 3.14

def drawPolygon(myTurtle, length, sides):
    angle = 360 / sides
    for x in range(sides):
        myTurtle.forward(length)
        myTurtle.left(angle)

def drawCircle(myTurtle, radius):
    circ = 2* pi * radius
    length = circ / 360
    drawPolygon(myTurtle, length, circ)
    
    
