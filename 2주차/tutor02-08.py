import turtle

import random

 

# 왼쪽 마우스버튼 클릭하여 도장찍기 함수

def screenLeftClick(x, y):

    global r, g, b

    r = random.random()

    g = random.random()

    b = random.random()

 

#크기는 1부터 5까지

    tSize = random.randrange(1, 6)

#각도는 0부터 360도 까지

    tAngle = random.randrange(0, 361)

 

#크기, 색상, 각도

    turtle.shapesize(tSize)

    turtle.color(r, g, b)

    turtle.right(tAngle)

#거북이 도장찍기

    turtle.stamp()

#거북이 이동

    turtle.penup()

    turtle.goto(x, y)

 

#변수 초기값

r, g, b = 0.0, 0.0, 0.0

 

#메인 부분

turtle.title("거북이 도장 찍는 프로그램")

turtle.shape("turtle")

turtle.onscreenclick(screenLeftClick, 1)

 

trutle.done()
