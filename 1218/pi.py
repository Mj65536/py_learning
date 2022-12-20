from random import random


def main():
    s = 20000000
    hits = 0
    for i in range(1, s):
        a, b = random(), random()
        r = pow(a ** 2 + b ** 2, 0.5)
        if r <= 1:
            hits += 1
    print("pi = {}".format((hits * 4) / s))


if __name__ == '__main__':
    main()
