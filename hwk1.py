import turtle
import keyboard

def main():
    tur = turtle.Turtle()
    '''
    #1.2
    star(tur)
    #1.3
    n = int(input("Enter the amount of points on the star: "))
    nstar(tur, n)
    #1.1
    numSquares = int(input("Enter the amount of squares: "))
    drawFlower(tur, numSquares)
    '''
    #1.4
    etchASketch(tur)


def star(t):
    t.left(72)
    t.forward(150)
    starTool(t, 36, 5)
    t.penup()

def starTool(t, angle, n):
    for _ in range(n-1):
        t.right(180-angle)
        t.forward(150)

def nstar(t, n):
    angle = 180/n
    t.left(n*2)
    t.forward(150)
    starTool(t, angle, n)

def drawSquare(t, sideLength):
    for _ in range(4):
        t.forward(sideLength)
        t.right(90)

def drawFlower(t, numSquares):
    angle = 360/numSquares
    for _ in range(numSquares):
        drawSquare(t, 100)
        t.right(angle)

def etchASketch(t):
    while True:
        try:
            if keyboard.is_pressed('w'):
                etchASketch_Forward(t)
            elif keyboard.is_pressed('a'):
                etchASketch_Left(t)
            elif keyboard.is_pressed('d'):
                etchASketch_Right(t)
        except:
            print('null')

def etchASketch_Forward(t):
    t.forward(2)

def etchASketch_Left(t):
    t.left(2)

def etchASketch_Right(t):
    t.right(2)


main()
turtle.Screen().exitonclick()