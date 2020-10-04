# Now we use Turtle module to draw things and make movement games
# please see the pics attached in the project to show the grid of screen of Ping pong Game 
import turtle 
###################################   create screen of game 
wind = turtle.Screen()     #    create window screen of the game 
wind.title("Ping Pong Game")    # create title of this screen 
wind.bgcolor("black")   # set color of the screen 
wind.setup(width=800,height=600)   # set width and height of the screen 
wind.tracer(0)  #  to control of the screen manually and stop update automatically 
##################################################################
# now create Game loop to make the game continue 

############## Now create the ball and  2 madrab 
# madrab 1
madrab1 = turtle.Turtle()   # to craete turtle object (Shape) and draw madrab1
madrab1.speed(0)   # to set speed at high speed of animation of drawing pixel in screen  
madrab1.shape("square")   # to set the square shape of madrab1
madrab1.color("blue")  # to set madarb1 color 
madrab1.shapesize(stretch_wid=5,stretch_len=1)  #to change shap size of madarab 1
madrab1.penup()  # to stop drwaing lines after movement
madrab1.goto(-350,0)

# madrab 2
madrab2 = turtle.Turtle()   # to craete turtle object (Shape) and draw madrab2  
madrab2.speed(0)   # to set speed at high speed of animation of drawing pixel in screen  
madrab2.shape("square")   # to set the square shape of madrab2
madrab2.color("red")  # to set madarb2 color 
madrab2.shapesize(stretch_wid=5,stretch_len=1)  #to change shap size of madarab 2
madrab2.penup()  # to stop drwaing lines after movement
madrab2.goto(350,0)
# ball
ball = turtle.Turtle()   # to craete turtle object (Shape) and draw ball
ball.speed(0)  # to set speed at high speed of animation of drawing pixel in screen  
ball.shape("square")   # to set the square shape of ball
ball.color("white")  # to set ball color 
ball.penup()  # to stop drwaing lines after movement
ball.goto(0,0)
ball.dx = 2.5 # delta x of ball  to control movement of ball of 2.5 move at x and 2.5 move at y 
ball.dy = 2.5 # delta y of ball  to control movement of ball of 2.5 move at x and 2.5 move at y 

score1 = 0
score2 = 0
score = turtle.Turtle()    # to craete turtle object (Shape) and draw Score
score.speed(0)    # to set speed at high speed of animation of drawing pixel in screen  
score.color("white")    # to set score object  color 
score.penup()      # to stop drwaing lines after movement
score.hideturtle()   # to hide score object 
score.goto(0,260)   # to set coordinates of score to appear in it 
score.write("Player 1 : 0 Player 2 : 0",align="center",font=("Courier",24,"normal"))
########################################################################
# functions to control of the madrab and ball movement

def madrab1_up():
    y = madrab1.ycor()   # get y corredinates of madrab1
    y += 20                    # increase y corrdinates by 20
    madrab1.sety(y)      # set the new y coordinates
def madrab1_down():
    y = madrab1.ycor()
    y -= 20                # decrease y coordinates by 20
    madrab1.sety(y)
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)
# Keyboard Bindings 
wind.listen()  # to allow the screen to be active and listen to any keyboard key has entered 
wind.onkeypress(madrab1_up,"w")  # to set the function madrab1_up to be active when I press on w key 
wind.onkeypress(madrab1_down,"s") # to set the function madrab1_down to be active when I press on s key 
wind.onkeypress(madrab2_up,"Up")  # Up is up arrow
wind.onkeypress(madrab2_down,"Down") # Down is down arrow

while True:
    wind.update() # update screen every time the game runs
    ball.setx(ball.xcor()+ball.dx)   # update x cooredinate of ball by delta x as 2.5 increment
    ball.sety(ball.ycor()+ball.dy)   # update x cooredinate of ball by delta y as 2.5 increment
    # border check 
    if ball.ycor() > 290:           # check if ball pass the screen border 
        ball.sety(290)              # set y coordinate of ball to 290 and reverse the movement
        ball.dy *= -1                # set y coordinate of ball to 290 and reverse the movement

    if ball.ycor() < -290:             # check if ball pass the screen border 
        ball.sety(-290)                  # set y coordinate of ball to -290 and reverse the movement
        ball.dy *= -1                     # set y coordinate of ball to -290 and reverse the movement
    
    if ball.xcor() > 390:             # check if ball pass the screen border 
        ball.goto(0,0)                   # set position of ball to (0,0)
        ball.dx *= -1                 # to revese the movement 
        score1 += 1       # indicate player 1  win the game 
        score.clear()      # to claer previous object before write new score object 
        score.write("Player 1 : {} Player 2 : {}".format(score1,score2),align="center",font=("Courier",24,"normal"))
    
    if ball.xcor() < -390:           # check if ball pass the screen border 
        ball.goto(0,0)               # set position of ball to (0,0)
        ball.dx *= -1                  # to revese the movement 
        score2 += 1       # indicate player 2  win the game 
        score.clear()      # to claer previous object before write new score object 
        score.write("Player 1 : {} Player 2 : {}".format(score1,score2),align="center",font=("Courier",24,"normal"))

    
    # Tasadom madrab and ball 
    if(ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
       
    
    if(ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
