def main():
    c = "ee#"
    d = "ee#"
    print(id(c) == id(d))
    # idle(交互模式)里驻留的标识符仅有下划线，字母数字，带有标识符的字符串有驻留机制，第一个输出与idle不同
    e = "ee_"
    f = "ee_"
    print(id(e) == id(f))
    g = ""
    h = ""
    print(id(g) == id(h))


if __name__ == '__main__':
    main()
