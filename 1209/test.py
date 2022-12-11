# coding=utf-8
import time


def main():
    # a = int(input('输入：'))
    # grade =
    # level = '+ -'
    # if a < 0 or a > 100:
    #     print('请输入一个0到100的数字')
    #     main()
    # else:
    #     if a <= 5:
    #         output = grade[6]+level[2]
    #     elif a < 10:
    #         output = grade[35]+grade[36]
    #     elif a < 15:
    #         output = grade[33]+grade[34]
    #     elif a < 20:
    #         output = grade[31]+grade[32]
    # print(grade)
    # s, b = 0, 1
    # while b <= 100:
    #     s += b
    #     b += 1
    # print(s)
    # for x in range(1, 10):
    #     for y in range(1, x+1):
    #         print('{} * {} = {}'.format(y, x, x*y), end='\t')
    #         time.sleep(0.3)
    #     print('\n')
    height = []
    number = 0
    sum_all = 0
    while True:
        h = input("请输入数据")
        if h.upper() == 'Q':
            print('记录结束')
            break
        elif not h.isdigit():
            print('请重新输入')
            continue
        else:
            number += 1
            height.append(h)
            sum_all += float(h)
            print('人数{}'.format(number))
            print('总和为{}'.format(sum_all))
            print('平均值为{}'.format(sum_all / number))


if __name__ == '__main__':
    main()
