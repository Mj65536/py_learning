import turtle


def nb():
    """
    this program is super cool
    this program is made in china


    """
    print("supercool")


def main():
    t = turtle.Pen()
    for x in range(1, 300, 3):
        t.forward(x)
        t.left(-78)
        nb()


if __name__ == '__main__':
    main()
