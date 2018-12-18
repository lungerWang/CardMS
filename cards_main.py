import cards_tools


while True:
    cards_tools.show_selection()
    action_str = input("Please select operation:")
    print("You select 【%s】" % action_str)
    if action_str in ["1", "2", "3"]:

        pass
    elif action_str == "0":
        print("Goodbye!")
        break
    else:
        print("Illegal selection!")