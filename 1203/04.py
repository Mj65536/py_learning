def main():
    import turtle
    turtle.width(4)
    turtle.color("blue", "red")
    turtle.begin_fill()
    turtle.forward(-400)
    for i in range(3, 12):
        turtle.circle(40, -360, steps=i)
        turtle.forward(100)
    turtle.circle(40)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
