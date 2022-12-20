import csv


def main():
    with open("学生信息表.csv", 'r', newline='') as stucsv:
        reader = csv.reader(stucsv)
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
