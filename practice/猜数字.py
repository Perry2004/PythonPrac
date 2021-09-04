def guess_number():
    range_ = int(input("请设置范围:"))
    import random
    y = random.randint (1,range_)

    x = int(input("本程序随机生成一个1-{}之间的整数，你猜是几:".format(range_)))
    z = 1
    while x != 0 or z ==1:
        if x == 0:
            print ("已退出程序，祝生活胜利")
            break
        elif y < x:
            print ("猜大了哦，再来一次吧")
            x = int(input("这次你猜几？"))
        elif y > x:
            print ("猜小了哦，再来一次吧")
            x = int(input("这次你猜几？"))
        elif y == x:
            print ("恭喜你猜对了")
            print ("感谢使用，祝生活顺利")
            break
guess_number()
