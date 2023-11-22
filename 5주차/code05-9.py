import turtle

##전역 변수 선언 부분##
swidth, sheight = 500, 500

##메인 코드 부분##
turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.goto(0, -sheight / 2)
turtle.pendown()
turtle.speed(10)

for radius in range(1, 250):
    if radius % 7 == 1 :
        turtle.pencolor('red')
    elif radius % 7 == 2 :
        turtle.pencolor('yellow')
    elif radius % 7 == 3 :
        turtle.pencolor('green')
    elif radius % 7 == 4 :
        turtle.pencolor('blue')
    elif radius % 7 == 5 :
        turtle.pencolor('navyblue')
    else :
        turtle.pencolor('purple')

    turtle.circle(radius)

turtle.done()
