from random import*


def main():
    a = randint(0, 100)
    t = 0
    while True:
        i = int(input("请输入一个0到100的整数："))
        t += 1
        if i < a:
            print("你猜的数字小于正确答案")
        elif i > a:
            print("你猜的数字大于正确答案")
        else:
            print(f"你猜了{t}次,猜对了,真厉害")
            break


if __name__ == '__main__':
    main()
