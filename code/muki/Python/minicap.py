'''import turtle
import random 


# gonna try to go for a maze of sorts.  will define obstacles through a field 

w = 800 # this is the width of the window in which the game will be played.  
h = 800 # this is the height of the play window
wall = 10 #width of the walls 
rate = 200 #time will be in ms

c_backround = ("green")
c_thing = ("red")
c_walls = ("black")
thing_direction = "up"

# class the_thing:
#     def __init__(self, "lets fill this with needed info !!!!! ")

def reset():    #this is the base fo stuff.
    global thing, thing_direction, obstacle_location, pen
    thing = [[0, 0]]
    thing_direction = "up"
    food_position = get_random_food_position()
    obstacle.goto(food_position)
    move_thing()
    return thing

def move_thing_up():
    global thing_direction                       
    if thing_direction != "down":
        thing_direction = "up"
    return

def move_thing_down():
    global thing_direction                       
    if thing_direction != "down":
        thing_direction = "up"
    return

def move_thing_left():
    global thing_direction                        
    if thing_direction != "down":
        thing_direction = "up"
    return

def move_thing_right():
    global thing_direction                
    if thing_direction != "down":
        thing_direction = "up"
    return

def collision():
    global obstacle_location
    if get_distance(thing[i], wall_location) < "thingsize":
        obstacle_location = get_random_obstacle_location()
        obstacle.goto(food_position)
        return True
    else:
        return False

def get_random_obstacle_location():
    return 



screen = turtle.Screen()

screen.listen()
screen.onkey(move_thing_up, "Up")
screen.onkey(move_thing_right, "Right")
screen.onkey(move_thing_down, "Down")
screen.onkey(move_thing_left, "Left")
screen.onkey(exit, "q")
screen.onkey(reset, "r") 


# screen = turtle.Screen()
screen.setup(w, h)
screen.title("Mine Field")
screen.bgcolor("cyan")
screen.setup(800, 800)
screen.tracer(0)
 

pen = turtle.Turtle("circle")
pen.pendown()
pen.penup()

# sides = 3
# edge_length = 0

# i = 0
# while i < 15:
# 	forward(edge_length)
# 	right(360/sides)
# 	i = i + 1
# 	edge_length = edge_length + 1

# from turtle import *
# import turtle

# obstacle = turtle.Turtle
# thing = turtle.Turtle
# walls = turtle.Turtle

# walls.forward(100)
# walls.right(90)
# walls.forward(100)
# walls.right(90)
# walls.forward(100)
# walls.right(90)
# walls.forward(100)
# walls.right(90)

turtle.done()'''
from turtle import *

i = 0
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1

done()