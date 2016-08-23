#Description: change on the traffic light occurs automatically
#the first traffic light use a cursor(turtle) to simulate the lights
#second traffic light place 3 turtles and turn them on and off with hideturtle() and showturtle()

import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

#first traffic light housing
draw_housing()

#draw second traffic light housing
tess.penup()
tess.forward(90)
tess.pendown()
draw_housing()

#return tess to first housing
tess.penup()
tess.back(90)

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")



#other turtles for second housing
#green_tess
green_tess = turtle.Turtle()
green_tess.penup()
green_tess.forward(130);
green_tess.left(90)
green_tess.forward(50)
green_tess.shape("circle")
green_tess.shapesize(3)
green_tess.fillcolor("black")


#orange_tess
orange_tess = turtle.Turtle()
#orange_tess.hideturtle()
orange_tess.penup()
orange_tess.forward(130)
orange_tess.left(90)
orange_tess.forward(120)
orange_tess.shape("circle")
orange_tess.shapesize(3)
orange_tess.fillcolor("black")

#red_tess
red_tess = turtle.Turtle()
#red_tess.hideturtle()
red_tess.penup()
red_tess.forward(130)
red_tess.left(90)
red_tess.forward(190)
red_tess.shape("circle")
red_tess.shapesize(3)
red_tess.fillcolor("black")


# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:        # Transition from state 0 to state 1
        tess.forward(70)      #first housing
        tess.fillcolor("orange")
        
        #orange_tess.showturtle()  #second housing
        #green_tess.hideturtle()
        orange_tess.fillcolor("orange")
        green_tess.fillcolor("black")
        state_num = 1 
        wn.ontimer(advance_state_machine, 300)   #The timer is restarted inside handler
    elif state_num == 1:                         # Transition from state 1 to state 2
        tess.forward(70)        #first housing
        tess.fillcolor("red")
        
        #red_tess.showturtle()   #second housing
        #orange_tess.hideturtle()
        red_tess.fillcolor("red")
        orange_tess.fillcolor("black")
        state_num = 2
        wn.ontimer(advance_state_machine, 3000)  #The timer is restarted inside handler
    else:                                        # Transition from state 2 to state 0
        tess.back(140)           #first housing
        tess.fillcolor("green")
        
        #green_tess.showturtle()    #second housing
        #red_tess.hideturtle()
        green_tess.fillcolor("green")
        red_tess.fillcolor("black")
        state_num = 0
        wn.ontimer(advance_state_machine, 2000)  #The timer is restarted inside handler

# Bind the event handler to the timer. The timer is restarted inside handler
#wn.onkey(advance_state_machine, "space")
#wn.listen()                      # Listen for events
advance_state_machine()
turtle.mainloop()
 
