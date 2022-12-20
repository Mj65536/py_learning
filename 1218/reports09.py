import time


def f(i):
    if i == 1:
        return 1
    else:
        return i * f(i - 1)


def main():
    for n in range(1, 31):
        print("{}的阶乘是{}".format(n, f(n)))
        time.sleep(0.5)


if __name__ == '__main__':
    main()
