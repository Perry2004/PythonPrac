choice_number = input("选项的数量是：")

import random

if choice_number == "2":
    a = input("你的第一个选项是")
    b = input("你的第二个选项是")
    list1 = [a,b]
    

elif choice_number == "3":
    a = input("你的第一个选项是")
    b = input("你的第二个选项是")
    c = input("你的第三个选项是")
    list1 = [a,b,c]

elif choice_number == "4":
    a = input("你的第一个选项是")
    b = input("你的第二个选项是")
    c = input("你的第三个选项是")
    d = input("你的第四个选项是")
    list1 = [a,b,c,d]

choice_ = str(random.sample (list1,1))
print ("你的选项是:",choice_)
