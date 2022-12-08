import os
import webbrowser


def hexo_g():
    generate = "hexo g"
    os.system(generate)


def hexo_d():
    deploy = "hexo d"
    os.system(deploy)


def hexo_n(title):
    new = f"hexo n \"{title}\""
    os.system(new)
    cmd = "start C:\\Progra~1\\Typora\\Typora.exe"
    os.system(cmd)


def hexo_s():
    server = "hexo s"
    webbrowser.open_new_tab("http://localhost:4000")
    os.system(server)


def hexo_c():
    clean = "hexo clean"
    os.system(clean)


def show():
    os.chdir('D:\\blog')
    menu = """
    ------------------------------------------------------------------------------------
    - 1.新建文章     - 2.预览      - 3.渲染      - 4.部署      - 5.清理缓存      - 6.退出    
    ------------------------------------------------------------------------------------
"""

    print(menu)

    opt = input("请输入要执行的操作: ")
    try:
        opt = int(opt)
    except IOError:
        print("输入类型有误")

    if opt not in range(1, 7):
        print('输入有误')
    else:
        if opt == 1:
            post_title = input("请输入文章标题: ")
            hexo_n(post_title)
            show()

        elif opt == 2:
            hexo_s()
            show()

        elif opt == 3:
            hexo_g()
            show()

        elif opt == 4:
            hexo_d()
            show()
        elif opt == 5:
            hexo_c()
            show()

        elif opt == 6:
            print('Goodbye')

        else:
            print('输入有误')


if __name__ == '__main__':
    show()
