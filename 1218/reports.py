def main():
    a = eval(input("请输入父亲身高(cm):"))
    b = eval(input("请输入母亲身高(cm):"))
    c = input("请选择小孩性别(M=男，F=女):")
    if c.upper() == 'M':
        print("预计小男孩身高为{}cm".format((a + b)*1.08/2))
    if c.upper() == 'F':
        print("预计小女孩身高为{}cm".format((a * 0.923 + b)/2))


if __name__ == '__main__':
    main()
