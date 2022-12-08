def main():
    a = (x*2 for x in range(1, 10))
    # print(a.__next__())
    # p = {'name': 'Pepe', 'age': '6', 'job': 'programmer'}

    # p['age'] = '8'
    # 新键值覆盖旧的 #

    # p['address'] = 'Shanghai'
    # 增加新的键值对 #

    # del(p['job'])
    # p.pop('age')
    # 删除特定键值对 #

    # p.clear()
    # 删除字典中全部键值对 #

    # print(p.keys())
    # print(p.values())
    # print(p.items())
    # print('name' in p)
    # print(len(p))
    # print(p['name'], p['age'], p['job'])
    # print(p.get('$', '60'))

    # print(p)

    # a, b, c = 1, 2, 3
    # (a, b, c) = (1, 2, 3)
    # a, b, c = (1, 2, 3)
    # [a, b, c] = [1, 2, 3]
    # print(a, b, c)

    # c1 = {'name': '小明一号', 'age': '12', 'job': '吃'}
    # c2 = {'name': '小明二号', 'age': '13', 'job': '喝'}
    # c3 = {'name': '小明三号', 'age': '14', 'job': '拉'}
    # c4 = {'name': '小明四号', 'age': '15', 'job': '睡'}
    # c5 = {'name': '小明五号', 'age': '16', 'job': '玩'}
    # t = [c1, c2, c3, c4, c5]
    # # print(t[0].get('name'))
    # for i in range(len(t)):
    #     print(t[i].get('name'), t[i].get('age'), t[i].get('job'))


if __name__ == '__main__':
    main()
