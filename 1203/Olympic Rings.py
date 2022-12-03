import turtle

turtle.setup(1280, 720)


def main():
    turtle.speed(6)
    turtle.shape("turtle")
    turtle.colormode(255)
    turtle.width(6)
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-120, 0)
    turtle.pendown()
    turtle.color(0, 0, 255)
    turtle.circle(50, 360, 32)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color(0, 0, 0)
    turtle.circle(50, 360, 32)
    turtle.penup()
    turtle.goto(120, 0)
    turtle.pendown()
    turtle.color(255, 0, 0)
    turtle.circle(50, 360, 32)
    turtle.penup()
    turtle.goto(-60, -60)
    turtle.pendown()
    turtle.color(255, 232, 0)
    turtle.circle(50, 360, 32)
    turtle.penup()
    turtle.goto(60, -60)
    turtle.pendown()
    turtle.color(0, 128, 64)
    turtle.circle(50, 360, 32)
    turtle.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
