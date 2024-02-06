
import turtle
import math
import random
import time
from types import NoneType

x_cord=-25
y_cord=80

class TurtleButton(turtle.Turtle):
    def __init__(self, width, height, action, text):
        super().__init__()
        self.width = width
        self.height = height
        self.action = action
        self.text = text
        self.penup()
        self.hideturtle()
        self.onclick(self.clicked)

    def draw_button(self, x, y):
        self.goto(x - self.width / 2, y - self.height / 2)
        self.fillcolor("white")
        self.begin_fill()
        for i in range(4):
            self.forward(self.width)
            self.left(90)
        self.end_fill()

        self.color("white")
        self.write(self.text, align="center", font=("Arial", 12, "normal"))
        self.showturtle()

    def clicked(self, x, y):
        self.action()

def draw_wheel():
    # Set up the turtle
    wheel_turtle = turtle.Turtle()
    wheel_turtle.speed(0)  # Set the turtle speed to the maximum
    
    # Draw the outer circle
    wheel_turtle.penup()
    wheel_turtle.color("black")
    wheel_turtle.goto(0, -100)  # Adjust the y-coordinate to move the wheel down
    wheel_turtle.pendown()
    wheel_turtle.circle(200)
    
    # Draw the numbers and colors on the wheel
    wheel_turtle.speed(10)
    for i in range(37):
        angle = i * (360 / 37)
        x = 160 * math.cos(math.radians(angle))
        y = 160 * math.sin(math.radians(angle))
        wheel_turtle.penup()
        wheel_turtle.goto(x, y + 90)  # Adjust the y-coordinate for each number
        wheel_turtle.pendown()
        
        if i == 0:
            wheel_turtle.color("lime")
        elif i % 2 == 1:
            wheel_turtle.color("red")
        else:
            wheel_turtle.color("black")
        
        wheel_turtle.write(str(i), align="center", font=("Arial", 12, "normal"))
       
    # Draw the black and red pockets
    for num in range(37):
        wheel_turtle.penup()
        angle = num * (360 / 37)
        x = 140 * math.cos(math.radians(angle))
        y = 140 * math.sin(math.radians(angle))
        if num == 0:
            color = "green"
        elif num % 2 == 0:
            color = "black"
        else:
            color = "red"
        wheel_turtle.goto(x, y+100)
        wheel_turtle.pendown()
        wheel_turtle.dot(12, color)
    wheel_turtle.hideturtle()
    
def spin_wheel():
    return random.randint(0, 36)

def respin():

    bet = -1
    colorBet = -1
    color = -1
    winnings = 0

    while colorBet != 0  and colorBet != 1:     #Taking an input for the bet
        try:
            colorBet = int(turtle.textinput("Place your bet", "Number or color? \n0. Number\n1. Color"))
        except ValueError or TypeError or NoneType:
            if NoneType:
                quit
            colorBet = -1
    if colorBet:
        while color != 0  and color != 1:
            try:
                color = int(turtle.textinput("Place your bet", "Which Color? \n0. Red\n1. Black"))
            except ValueError or TypeError or NoneType:
                if NoneType:
                    quit
                color = -1
    else:
        while bet < 0 or bet > 36:
            try: 
                bet = int(turtle.textinput("Welcome to Roulette!", "What would you like to bet on?"))
            except ValueError or TypeError:
                    if None:
                        quit
                    bet = -1

    result = spin_wheel()

    if result == 0:
        turtleColor = "green"
    elif result % 2 == 1:
        turtleColor = "red"
        if color == 0:
            winnings = 1
    else:
        turtleColor = "Black"
        if color == 1:
            winnings = 1

    if bet == result:
        winnings = 5
    
    turtle.clear()  # Clear previous result
    turtle.penup()
    turtle.color(turtleColor)
    turtle.goto(x_cord, y_cord)
    turtle.pendown()
    turtle.write(f"{result}", font=("Bauhaus 93", 40, "normal"))
    turtle.hideturtle()
    print(f"\nSpinning the wheel... The result is {result}.")

    time.sleep(.5)

    if winnings > 0:       #check if the user won the round
        turtle.clear()
        turtle.penup()
        turtle.goto(50,80)
        turtle.pendown()
        turtle.color("blue")
        turtle.write(f"You win!", font=("Bauhaus 93", 40, "normal"))
        print("You win!")
    else: 
        turtle.clear()
        turtle.penup()
        turtle.goto(-175,80)
        turtle.pendown()
        turtle.color("yellow")
        turtle.write(f"Sorry, try again", font=("Bauhaus 93", 40, "normal"))
        print("Sorry, try again")


turtle.Screen().bgcolor("dark green")
draw_wheel()

respin_button = TurtleButton(width=0, height=0, action=respin, text="Spin")
respin_button.draw_button(0, -10)

respin()

turtle.done()

