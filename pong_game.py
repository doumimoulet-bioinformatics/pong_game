import turtle    #imported turtle module
wind= turtle.Screen() #initialize screen
wind.title("ping pong game") #set the title of the window
wind.bgcolor("black") # set the background color of the window
wind.setup(width=800,height=600) # set the width and height of the window
wind.tracer(0) # stops the window from updating automatically 
#padle1
padle1= turtle.Turtle() #initializes turtle object(shape)
padle1.speed(0) # set speed for the animation
padle1.shape("square") # set the shape of the object 
padle1.color("blue") # set the color of the shape 
padle1.shapesize(stretch_wid=5,stretch_len=1) # stretches the shape to the wanted size
padle1.penup() # stops the object from drawing lines 
padle1.goto(-350,0) # set the position of the object 
#padle2
padle2= turtle.Turtle()
padle2.speed(0)
padle2.shape("square")
padle2.color("red")
padle2.shapesize(stretch_wid=5,stretch_len=1)
padle2.penup()
padle2.goto(350,0)
#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4

#score 
score1= 0
score2= 0
score= turtle.Turtle()
score.speed(0)
score.color("green")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player1: 0 player2: 0", align="center", font=("courier",24,"normal"))
#functions
def padle1_up():
    y = padle1.ycor() #get the y coordinates of padle1
    y += 20 #set the y to increase by 20
    padle1.sety(y) #set the y of padle1 to the new y coordinates
def padle1_down():
    y = padle1.ycor()
    y -= 20 #set the y to decrease by 20
    padle1.sety(y)
def padle2_up():
    y = padle2.ycor()
    y += 20
    padle2.sety(y)
def padle2_down():
    y = padle2.ycor()
    y -= 20
    padle2.sety(y)
#keyboard bindings
wind.listen()  # tell the window to expect keyboard input
wind.onkeypress(padle1_up,"w") #when pressing w padle1_up is invoked
wind.onkeypress(padle1_down,"s")
wind.onkeypress(padle2_up,"Up")
wind.onkeypress(padle2_down,"Down")

#main game loop
while True: # main game loop
    wind.update() #updates the screen everytime the loop runs
    #move the ball
    ball.setx(ball.xcor()+ ball.dx) #ball starts at 0 and everytime the loop runs --->+0.4xaxis
    ball.sety(ball.ycor()+ ball.dy) #ball starts at 0 and everytime the loop runs --->+0.4 xaxis
    #border check top border +300px, bottom border -300px , ball is 20 px
    if ball.ycor() > 290: #if ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1 #reverse direction, +0.4 --->-0.4
    if ball.ycor() < -290: #if ball is at bottom border 
            ball.sety(-290)
            ball.dy *= -1
    if ball.xcor() > 390: #if ball is at thr right border 
         ball.goto(0, 0) #return ball to center 
         ball.dx *= -1 #reverse the x direction
         score1 += 1
         score.clear()
         score.write("player1: {} player2: {} ".format(score1,score2) , align="center", font=("courier",24,"normal"))
    if ball.xcor() < -390: #if ball is at left border
             ball.goto(0, 0)
             ball.dx *= -1
             score2 += 1
             score.clear()
             score.write("player1: {} player2: {} ".format(score1,score2) , align="center", font=("courier",24,"normal"))
    #the point where the ball and padle meet
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()< padle2.ycor() + 40 and ball.ycor()> padle2.ycor() -40):
         ball.setx(340)
         ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()< padle1.ycor() + 40 and ball.ycor()> padle1.ycor() -40):
             ball.setx(-340)
             ball.dx *= -1

