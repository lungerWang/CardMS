# 存储名片的字典列表
card_list = []


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
    print("-" * 50)
    print("new card")
    name = input("请输入姓名：")
    tel = input("请输入电话：")
    qq = input("请输入qq：")
    email = input("请输入邮箱")
    card_dict = {"name": name, "tel": tel, "qq": qq, "email": email}
    card_list.append(card_dict)
    print("添加联系人名片 %s 成功" % name)
    print(card_list)


def all_card():
    print("-" * 50)
    print("all card")


def search_card():
    print("-" * 50)
    print("search card")
