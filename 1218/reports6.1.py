from random import*


def main():
    a = randint(0, 100)
    t = 0
    maxcount = 20
    while maxcount >= 1:
        i = int(input("请输入一个0到100的整数："))
        t += 1
        maxcount -= 1
        if i < a:
            print(f"你猜的数字小于正确答案,还有{maxcount}次机会")
        elif i > a:
            print(f"你猜的数字大于正确答案,还有{maxcount}次机会")
        else:
            print(f"你猜了{t}次,猜对了,真厉害")
            break
    else:
        print("给你机会你不中用啊!")


if __name__ == '__main__':
    main()
