def main():
    a = 13
    i = 2022
    while a < 26:
        a = a * 1.008
        i += 1
    print(f"预计我国人口将在第{i}年,即{i-2022}年后到达26亿")


if __name__ == '__main__':
    main()
