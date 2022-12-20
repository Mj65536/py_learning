def main():
    a = eval(input("请输入体重(kg):"))
    b = eval(input("请输入身高(cm):"))
    c = eval('%.3f' % (a / ((b / 100) ** 2)))
    if c < 18.5:
        print(f'BMI指数为{c}, 判断为体重过低')
    elif c <= 24:
        print(f'BMI指数为{c}, 判断为正常范围')
    elif c < 27:
        print(f'BMI指数为{c}, 判断为肥胖前期')
    elif c < 30:
        print(f'BMI指数为{c}, 判断为Ⅰ度肥胖')
    elif c < 40:
        print(f'BMI指数为{c}, 判断为Ⅱ度肥胖')
    else:
        print(f'BMI指数为{c}， 判断为Ⅲ度肥胖')


if __name__ == '__main__':
    main()
