import jieba


def main():
    txt = '''
木兰花·拟古决绝词柬友
【清】·纳兰性德
人生若只如初见，何事秋风悲画扇。
等闲变却故人心，却道故人心易变。
骊山语罢清宵半，泪雨霖铃终不怨。
何如薄幸锦衣郎，比翼连枝当日愿。
'''
    words = jieba.lcut(txt)
    print(words)

    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1
    print(counts)

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for item in items:
        # print(item)
        print("{}出现了{}次".format(item[0], item[1]))


if __name__ == '__main__':
    main()
