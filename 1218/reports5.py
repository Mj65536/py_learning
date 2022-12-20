def main():
    i = 7
    while True:
        if i % 7 == 0 and i % 6 == 5 and i % 5 == 4 and i % 3 == 2 and i % 2 == 1:
            print(f"该阶梯最少有{i}阶")
            break
        else:
            i = i + 7


if __name__ == '__main__':
    main()
