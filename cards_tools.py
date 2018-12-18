# 存储名片的字典列表
card_list = [{"name": "Micheal", "tel": "213456", "qq": "9123901", "email": "Micheal@163.com"},
             {"name": "Kat", "tel": "8998664", "qq": "112912147", "email": "Kat@qq.com"}
             ]


def print_card_head():
    """输出表头"""
    for head in ["姓名", "电话", "QQ", "邮箱"]:
        print(head, end="\t\t")


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

    print_card_head()

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
    # 提示用户输入要查找的名字
    search_name = input("Please input name:")

    # 遍历列表查找
    for card_dict in card_list:
        if search_name == card_dict["name"]:
            print_card_head()
            # 分割线
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["tel"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("card not found")


def deal_card(card_dict):
    action_str = input("请选择要进行的操作：1.修改   2.删除   0.返回上级菜单:")
    if action_str == "1":
        print("请输入新的字段信息，回车表示不修改")
        card_dict["name"] = input_card_info(card_dict["name"], "name:")
        card_dict["tel"] = input_card_info(card_dict["tel"], "tel:")
        card_dict["qq"] = input_card_info(card_dict["qq"], "qq:")
        card_dict["email"] = input_card_info(card_dict["email"], "email:")
        pass
    elif action_str == "2":
        card_list.remove(card_dict)
        print("删除成功")


def input_card_info(default, hint):
    """
    获取输入信息
    :param default: 默认值
    :param hint: 提示信息
    :return: 如果输入空，则用默认值，不为空则使用输入的值
    """
    input_str = input(hint)
    if len(input_str) == 0:
        return default
    else:
        return input_str
