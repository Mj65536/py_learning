import time


def main():
    t1 = time.time()
    for i in range(1000):
        result = []
        for m in range(10000):
            result.append(i * 1000 + m * 100)
    t2 = time.time()
    print(t2 - t1)


if __name__ == '__main__':
    main()
