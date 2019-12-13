import turtle as tu

turtle = tu

turtle.shape('classic')
turtle.mode('logo')
turtle.speed(5)

def moveTo (posX, posY):
    turtle.up()
    turtle.goto(posX, posY)

def drawRect(posX, posY, sizeX, sizeY, color='grey'):
    moveTo(posX, posY)
    turtle.down()
    turtle.color(color)
    turtle.right(90)
    turtle.forward(sizeX)
    turtle.right(90)
    turtle.forward(sizeY)
    turtle.right(90)
    turtle.forward(sizeX)
    turtle.right(90)
    turtle.forward(sizeY)

def drawTriangleIso(upperAngleX, upperAngleY, baseSize, facing = 0, color='grey'):
    moveTo(upperAngleX, upperAngleY)
    turtle.seth(facing)
    turtle.down()
    turtle.color(color)
    turtle.right(30)
    turtle.forward(baseSize)
    turtle.right(30 + 90)
    turtle.forward(baseSize)
    turtle.right(30 + 90)
    turtle.forward(baseSize)

def drawHexa(posX, posY, sideSize, angle = 0, color='grey'):
    moveTo(posX, posY)
    for x in range(6):
        drawTriangleIso(posX, posY, sideSize, -60*x + angle - 30, color)

def drawLine(posX, posY, endX, endY, color='grey'):
    moveTo(posX, posY)
    turtle.down()
    turtle.color(color)
    turtle.goto(endX, endY)



### USE IT FOR DEBUG : 

# for i in range(40):
#     drawLine(i*10, -400, i*10, 400, "grey")
#     drawLine(-i*10, -400, -i*10, 400, "grey")
# for i in range(40):
#     drawLine(-400, -i*10, 400, -i*10, "grey")
#     drawLine(-400, i*10, 400,i*10, "grey")

# drawLine(0, -400, 0, 400, "red")
# drawLine( -400, 0, 400, 0, "red")

turtle.width(5)
drawLine(-400, -300, 400, -300, "grey")
turtle.width(3)

drawLine(300, -300, 300, -150, "brown")
drawLine(300,-150, 200, -100, "brown")
drawHexa(200, -100, 55, -4, 'green')

drawLine(300,-150, 300, 10, "brown")
drawLine(300, 10, 200, 50, "brown")
drawHexa(200, 50, 55, -9, 'green')

drawLine(300, 10, 300, 200, "brown")
drawHexa(300, 200, 80, 0, 'green')
size = 30





wheelSize= 65
drawHexa(-250,-300+wheelSize, wheelSize, 0, 'yellow')
drawLine(-250,-300+wheelSize, -180, -110, "orange")

drawLine(-180, -110, -140, -70, "red")

drawLine(-30, -110, 10, -70, "red")
drawLine(10, -70, -35, -70, "red")


drawTriangleIso(-180, -110,150, 60, "orange")
drawTriangleIso(-180 + 75, -110 -130,150, 0, "orange")

drawHexa(45,-305+wheelSize, wheelSize, 40, 'yellow')


drawHexa(-200,200, size, 0, 'cyan')
drawHexa(-120,150, size, 0, 'cyan')
drawHexa(-40,200, size, 0, 'cyan')
drawHexa(40,150, size, 0, 'cyan')


moveTo(-380, -300)
turtle.color('black')
turtle.seth(90)
turtle.shape('turtle')

turtle.done()
input()