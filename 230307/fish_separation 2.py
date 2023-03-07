def main():
    i = 1
    n = 5 * i + 1
    a1 = (n-1) / 5
    a2 = (n - a1 - 2) / 5
    a3 = (n - a1 - a2 - 3) / 5
    a4 = (n - a1 - a2 - a3 - 4) / 5
    a5 = (n - a1 - a2 - a3 - a4 - 5) / 5
    while 1:
        if not (a5*5) % 5 == 0:
            i += 1
            n = 5 * i + 1
            a1 = (n - 1) / 5
            a2 = (n - a1 - 2) / 5
            a3 = (n - a1 - a2 - 3) / 5
            a4 = (n - a1 - a2 - a3 - 4) / 5
            a5 = (n - a1 - a2 - a3 - a4 - 5) / 5
        else:
            print(f'第一个人醒来后看到{n}条鱼')
            print(f'第二个人醒来后看到{int(a2 * 5 + 1)}条鱼')
            print(f'第三个人醒来后看到{int(a3 * 5 + 1)}条鱼')
            print(f'第四个人醒来后看到{int(a4 * 5 + 1)}条鱼')
            print(f'第五个人醒来后看到{int(a5 * 5 + 1)}条鱼')
            break


if __name__ == '__main__':
    main()
