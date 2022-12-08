def main():
    a = int(input('输入：'))
    grade = ''
    if a < 60:
        grade = '歌姬'
    elif a < 80:
        grade = '6'
    elif a <= 100:
        grade = 'NB'


if __name__ == '__main__':
    main()
