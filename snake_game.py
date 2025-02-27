import turtle
import random
import time

# create screen

screen=turtle.Screen()
screen.title('Snake.io')
screen.setup(width=600,height=600)
screen.tracer(8)
screen.bgcolor('black')

# creat boarder

turtle.speed(0)
turtle.pensize(5)
turtle.penup()
turtle.goto(-290,-290)
turtle.pendown()
turtle.color('red')
turtle.forward(580)
turtle.right(90)
turtle.forward(580)
turtle.right(90)
turtle.forward(580)
turtle.right(90)
turtle.forward(580)
turtle.right(90)
turtle.forward(580)
turtle.hideturtle()

#score

score=0
delay=0.1

#snake

snake=turtle.Turtle()
snake.speed(0)
snake.shape('circle')
snake.color('pink')
snake.penup()
snake.goto(0,0)
snake.direction='stop'

#food

food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('blue')
food.penup()
food.goto(0,100)
old_food=[]


#scoring

scoring=turtle.Turtle()
scoring.speed(0)
scoring.color('white')
scoring.penup()
scoring.hideturtle()
scoring.goto(0,256)
scoring.write('Score:',align='left',font=('Liter',18,'bold'))

#function of motion

def snake_go_up():
    if snake.direction != 'down':
        snake.direction='up'

def snake_go_down():
    if snake.direction != 'up':
        snake.direction='down'

def snake_go_right():
    if snake.direction != 'left':
        snake.direction='right'

def snake_go_left():
    if snake.direction != 'right':
        snake.direction='left'

def move():

    if snake.direction == 'up':
        y=snake.ycor()
        snake.sety(y+20)

    if snake.direction == 'down':
        y=snake.ycor()
        snake.sety(y-20)

    if snake.direction == 'right':
        x=snake.xcor()
        snake.setx(x+20)

    if snake.direction == 'left':
        x=snake.xcor()
        snake.setx(x-20)

#keyboard binding

screen.listen()
screen.onkey(snake_go_up,'Up')
screen.onkey(snake_go_down,'Down')
screen.onkey(snake_go_right,'Right')
screen.onkey(snake_go_left,'Left')

#main game loop
while True:
    screen.update()
    if snake.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        score+=1
        scoring.clear()
        scoring.write('SCORE:{}'.format(score),align='left',font=('Liter',18,'bold'))
        delay-=0.001
        new_food=turtle.Turtle()
        new_food.speed(0)
        new_food.shape('circle')
        new_food.color('blue')
        new_food.penup()
        new_food.goto(0,100)
        old_food.append(new_food)
    

    for index in range (len(old_food)-1,0,-1):
        a=old_food[index-1].xcor()
        b=old_food[index-1].ycor()
        old_food[index].goto(a,b)

    if len(old_food)>0:
        old_food[0].goto(snake.xcor(),snake.ycor())
    move()
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0,0)
        scoring.write('GAME OVER \n YOUR SCORE:{}'.format(score),font=('Liter',18,'bold'),align='center')

    for i in old_food:
        if i.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0,0)
            scoring.write('GAME OVER \n YOUR SCORE:{}'.format(score),font=('Liter',18,'bold'),align='center')
        
    time.sleep(delay)
turtle.done()