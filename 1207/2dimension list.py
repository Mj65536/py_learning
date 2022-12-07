def main():
    a = [
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
            [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
            [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
        ]

    # a.extend(list(range(11, 21)))
    # b = [i**4 for i in range(1, 11)]
    # print(a.count(5))
    # c = a.sort(reverse=True)
    # print(c)
    # print(a.reverse())
    # print(a)
    # print(a.sort(reverse=True))
    for x in range(3):
        for y in range(10):
            print(a[x][y], end=' ')
        print('\n')
    print("打印完成")


if __name__ == '__main__':
    main()
