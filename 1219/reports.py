import jieba

txt = open("红楼梦.txt", "r", encoding="utf-8").read()
excludes = {"什么", "一个", "我们", "那里", "如今", "你们", "说道", "知道", "起来", "这里",
            "出来", "姑娘", "他们", "众人", "奶奶", "自己", "一面", "只见", "两个",
            "怎么", "不是", "不知", "这个", "听见", "这样", "进来", "咱们", "告诉", "就是",
            "东西", "回来", "大家", "没有", "只是", "这样", "进来", "咱们", "告诉", "就是"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "老太太" or word == "太太" or word == "老祖宗" or word == "史太君":
        rword = "贾母"
    elif word == "老爷":
        rword = "贾政"
    elif word == "宝二爷":
        rword = "宝玉"
    elif word == "王熙凤" or word == "熙凤" or word == "凤辣子":
        rword = "凤姐"
    elif word == "林黛玉" or word == "潇湘妃子" or word == "林丫头" or word == "林妹妹":
        rword = "黛玉"
    elif word == "宝姑娘" or word == "宝丫头" or word == "蘅芜君" or word == "宝姐姐":
        rword = "宝钗"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1

for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
print("全部人物出场次数")
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
