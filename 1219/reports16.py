def book():
    menu = '''
    请选择操作：
    1 = 添加
    2 = 查询
    3 = 退出
    '''
    while True:
        opt = ''
        try:
            opt = int(input(menu))
        except TypeError:
            print("输入有误")
            book()
        except ValueError:
            print("输入有误")
            book()
        except KeyboardInterrupt:
            print("")
            book()
        except EOFError:
            print("")
            book()

        if opt == 3:
            break
        elif opt == 1:
            new = input("请输入要添加的单词和释义：")
        elif opt == 2:
            word = input("请输入要查询的单词：")
            with open('book.txt', 'a+') as txt:
                r = txt.readline()


if __name__ == '__main__':
    book()
