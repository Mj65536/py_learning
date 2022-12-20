import turtle

turtle.setup(1280, 720)


def main():
    turtle.speed(6)
    turtle.shape("turtle")
    turtle.width(6)
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-110, -25)
    turtle.pendown()
    turtle.color("blue")
    turtle.circle(45)
    turtle.penup()
    turtle.goto(0, -25)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(45)
    turtle.penup()
    turtle.goto(110, -25)
    turtle.pendown()
    turtle.color("red")
    turtle.circle(45)
    turtle.penup()
    turtle.goto(-55, -75)
    turtle.pendown()
    turtle.color("yellow")
    turtle.circle(45)
    turtle.penup()
    turtle.goto(55, -75)
    turtle.pendown()
    turtle.color("green")
    turtle.circle(45)
    turtle.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
