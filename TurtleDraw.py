import turtle

# Turtle Draw
# Author: Nick Paugys

print("Turtle Draw Starting...")

TEXTFILENAME = 'turtle-draw.txt'
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()

while line:
    print(line, end="")
    line = turtleDrawTextfile.readline()

edTheTurtle = turtle.Turtle()
edTheTurtle.forward(100)
edTheTurtle.right(90)
edTheTurtle.forward(100)
edTheTurtle.right(90)
edTheTurtle.forward(100)
edTheTurtle.right(90)
edTheTurtle.forward(100)

spiral = turtle.Turtle()

for i in range(40):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()