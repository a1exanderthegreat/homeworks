from turtle import*
speed(100)

def square():
    for i in range(4):
        forward(200)
        left(90)
 
square()


def karebi():
    forward(60)
    left(90)
    for i in range(3):
        forward(90)
        right(90)

karebi()

penup()
goto(200,200)
pendown()

# roof

right(50)
forward(140)
left(94)
forward(154)
left(46)
#window

penup()
goto(140,160)
pendown()

def window():
    for i in range(4):
      forward(50)
      left(90)  

window()

penup()
goto(15,160)
pendown()

def window1():
    for i in range(4):
        forward(50)
        left(90)

window1()



exitonclick()