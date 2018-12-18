# 存储名片的字典列表
card_list = [{"name": "Micheal", "tel": "213456", "qq": "9123901", "email": "Micheal@163.com"},
             {"name": "Kat", "tel": "8998664", "qq": "112912147", "email": "Kat@qq.com"}
             ]


def show_selection():
    print("*" * 50)
    print("Welcome to 【CardSystem】 V1.0")
    print("")
    print("1.Add card")
    print("2.Show cards")
    print("3.Search card")
    print("")
    print("0.Exit")
    print("*" * 50)


def new_card():
    """创建新名片"""
    print("-" * 50)
    print("new card")

    # 提示用户输入信息
    name = input("请输入姓名：")
    tel = input("请输入电话：")
    qq = input("请输入qq：")
    email = input("请输入邮箱")

    # 创建联系人字典
    card_dict = {"name": name,
                 "tel": tel,
                 "qq": qq,
                 "email": email}

    card_list.append(card_dict)
    print("添加联系人名片 %s 成功" % name)
    print(card_list)


def show_all_card():
    """查看所有名片"""
    # 判断非空
    if len(card_list) == 0:
        print("请先添加名片")
        return

    print("-" * 50)
    print("all card")

    # 输出表头
    for head in ["姓名", "电话", "QQ", "邮箱"]:
        print(head, end="\t\t")

    # 分割线
    print("")
    print("=" * 50)

    # 遍历联系人
    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card["name"],
                                        card["tel"],
                                        card["qq"],
                                        card["email"]))


def search_card():
    """查询名片"""
    print("-" * 50)
    print("search card")
