import csv


def main():
    with open("学生信息表.csv", 'a+', newline='') as stucsv:
        writer = csv.writer(stucsv)
        writer.writerow(['10080108', '虚竹', '男', '武学18-1'])


if __name__ == '__main__':
    main()
