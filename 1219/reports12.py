def search():
    database = {"10080101": {"姓名": "杨过", "班级": "武学18-1班"},
                "10080202": {"姓名": "郭靖", "班级": "武学18-2班"},
                "10080301": {"姓名": "段誉", "班级": "武学18-3班"}}
    a = input("请输入要查询的学号：")
    if a not in database.keys():
        print("没有学号为{}的学生".format(a))
    else:
        print("学号为{}的同学{}在{}".format(a, database.get(a).get("姓名"), database[a]["班级"]))


if __name__ == '__main__':
    search()
