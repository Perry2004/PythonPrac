print("Hello")
your_name = input("What's your name:")

if your_name == "Perry":
    print("Hello")
    password_ = input("Password:")
    if password_ == ("040205"):
        print("Welcome", your_name, sep=',')
        import random
        lucky_value = random.randint(1, 100)
        lucky_value = str(lucky_value)
        print("今天你的幸运值是" + lucky_value)

        if lucky_value >= '85':
            print("今天运气不错哦")
        elif lucky_value == '100':
            print("今天运气爆棚哦!")
        elif lucky_value >= '45':
            print("今天是寻常的一天")
        elif lucky_value < '45':
            print("今天运气不太好哦")
        print("Thank you for using your first program.")
        print("Have a good day!")
        print()
    else:
        print("Wrong password")
else:
    print("Sorry, you do not have access to this program.")
