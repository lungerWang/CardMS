import cards_tools


while True:
    # 显示名片系统操作选项
    cards_tools.show_selection()

    # 获取并判断用户的输入
    action_str = input("Please select operation:")
    print("You select 【%s】" % action_str)
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools.new_card()

        elif action_str == "2":
            cards_tools.show_all_card()

        elif action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":
        print("Goodbye!")
        break
    else:
        print("Illegal selection!")

