import turtle
import math

# Turtle Draw
# Author: Nick Paugys

print("Turtle Draw Starting...")

nickTheTurtle = turtle.Turtle()
nickTheTurtle.speed("fastest")
nickTheTurtle.penup()

user_input = input("Insert name of file: ")
print(f"Opening {user_input}")

turtleWindow= turtle.Screen()
turtleWindow.setup(450, 450)

TEXTFILENAME = 'turtle-draw.txt'
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()

def close_window():
    turtle.bye()

turtleWindow.onkey(close_window, 'Return')
turtleWindow.listen()

def distance_formula(point1, point2):
    magnitude = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) **2)
    return magnitude

green = 0
blue = 0
black = 0
red = 0
blue_value = 0
green_value = 0
red_value = 0
black_value = 0

previous_data = 0
current_data = 0

def distance_by_color(point1, point2):
    if segments[0] == "green":
        green_value = distance_formula(point1, point2)
        green = green + green_value
    
    elif segments[0] == "blue":
        blue_value = distance_formula(point1, point2)
        blue = blue + blue_value
    
    elif segments[0] == "red":
        red_value = distance_formula(point1, point2)
        red = red + red_value
    
    elif segments[0] == "black":
        black_value = distance_formula(point1, point2)
        black = black + black_value
    
    else:
        pass
        
         
def calculate_total_distance(points):
    total_distance = 0
    for i in range(len(points) - 1):
        distance = distance_formula(points[i], points[i + 1])
        total_distance += distance
    return total_distance

while line:
    print(line, end="")
    segments = line.split(' ')

    current_data = segments

    if (len(segments) == 3):
        color = segments[0]
        x_coordinate = int(segments[1])
        y_coordinate = int(segments[2])
        nickTheTurtle.color(color)
        nickTheTurtle.goto(x_coordinate,y_coordinate)
        nickTheTurtle.pendown()
    
    elif (len(segments) != 3):
        nickTheTurtle.penup()

    distance_by_color(previous_data, current_data)
    
    previous_data = current_data

    line = turtleDrawTextfile.readline()

turtleDrawTextfile.close()   
turtle.done()
print(f"\n\nTotal distance of blue lines: {blue_value}")
print(f"\nTotal distance of green lines: {green_value}")
print(f"\nTotal distance of red lines: {red_value}")
print(f"\nTotal distance of black lines: {black_value}")
print(F"\nTotal distance traveled by nickTheTurtle: {calculate_total_distance}")
print("\nTurtle Draw Complete.")
