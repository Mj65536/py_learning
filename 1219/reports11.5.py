import random


def rock_scissors_paper():
    gestures = ("石头", "剪刀", "布")
    win_cases = (['石头', '剪刀'], ['剪刀', '布'], ['布', '石头'])
    # 元组里面放列表，列表不用加引号
    menu = '''
请输入选项:
1 = 石头        
2 = 剪刀        
3 = 布          
4 = 退出游戏     
'''
    while True:
        try:
            ugestures = int(input(menu))
            cgestures = random.choice(["石头", "剪刀", "布"])
        except TypeError:
            print("输入类型有误，请重新输入")
            continue
        except ValueError:
            print("输入类型有误，请重新输入")
            continue

        if ugestures == 4:
            print('游戏结束')
            break
        elif ugestures not in [1, 2, 3, 4]:
            print('请选择1到4范围内的数字')
            continue
        else:
            print('你选择了:{}\n电脑选择了:{}'.format(gestures[int(ugestures) - 1], cgestures))
            if gestures[int(ugestures) - 1] == cgestures:
                print("平局")
            elif [gestures[int(ugestures) - 1], cgestures] in win_cases:
                print("你赢了")
            else:
                print('你输了')


if __name__ == '__main__':
    rock_scissors_paper()
