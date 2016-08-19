import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

pensize = tess.pensize()

#this are all posible shapes according to the help doc
cursor_shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
cursor_shape = tess.shape()    #storage current shape

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

def h5():
    tess.color("red")

def h6():
    tess.color("green")

def h7():
    tess.color("blue")

def h8():
    global pensize
    if pensize < 20:
       pensize+=1
       wn.title(pensize)
       tess.pensize(pensize)

def h9():                    
    global pensize
    if pensize > 1:
       pensize-=1
       wn.title(pensize)
       tess.pensize(pensize)       

def h10():                     #change the cursor shape
    global cursor_shapes
    global cursor_shape
    if cursor_shape < len(cursor_shapes)-1:  #is cursor_shape not the last shape 
       cursor_shape+=1
    else:
       cursor_shape=0       
       
    tess.shape(cursor_shapes[cursor_shape])
    
    
    

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")
wn.onkey(h8, "+")
wn.onkey(h9, "-")
wn.onkey(h10, "s")  #turtle shape

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
turtle.mainloop()
