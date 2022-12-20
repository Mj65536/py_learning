def is_prime():
    a = int(input("请输入要判断的正整数"))
    if a <= 1:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        else:
            return True


def main():
    print(is_prime())


if __name__ == '__main__':
    main()
