def root(a):
    x0 = a / 2
    while True:
        x1 = (x0 + a / x0) / 2
        if abs(x1 - x0) < 1e-6:
            break
        x0 = x1
    return x0


def main():
    n = eval(input("请输入要开方的数："))
    print('%.6f' % root(n))


if __name__ == '__main__':
    main()
