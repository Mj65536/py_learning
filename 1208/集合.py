def main():
    a = {1, 2, 3, 4, 5, 6}
    a.add(7)
    print(a)
    b = {3, 4, 4, 3, 5, 6, 7, 8}
    b.remove(6)
    print(b)
    print(a | b, a & b, a - b, a.union(b), a.intersection(b), a.difference(b))
    # 后三个依次等价于前三个
    # set()将可迭代对象转化为集合，集合中相同元素只保留一个


if __name__ == '__main__':
    main()
