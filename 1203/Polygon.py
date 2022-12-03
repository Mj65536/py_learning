def main():
    import turtle
    turtle.setup(1920, 720)
    turtle.shape("turtle")
    turtle.width(4)
    turtle.color("blue", "yellow")
    turtle.begin_fill()
    turtle.penup()
    turtle.forward(-800)
    turtle.pendown()
    for i in range(5, 16):
        turtle.circle(60, -360, steps=i)
        turtle.penup()
        turtle.forward(150)
        turtle.pendown()
    turtle.circle(60, -360)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
