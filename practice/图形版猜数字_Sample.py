import tkinter as tk
import random as rd

window_one = tk.Tk()
window_one.title('图形版猜数字')
window_one.geometry('400x200')

n = rd.randint(1,100)
def guess():
    gn = int(entry_one.get())
    if gn==n:
        label_two['text'] = '恭喜你猜对了'
        label_two.update()
    elif gn < n:
        label_two['text'] = '猜小了哦，再来一次吧'
        label_two.update()
    else: 
        label_two['text'] = '猜大了哦，再来一次吧'
        label_two.update()
    
label_one = tk.Label(window_one, text='本程序随机生成一个1-100之间的整数\n你猜是几：')
label_two = tk.Label(window_one, text='答题结果')
entry_one = tk.Entry(window_one)
button_one = tk.Button(window_one, text='猜一下', command=guess)

label_one.pack()
entry_one.pack()
button_one.pack()
label_two.pack()
window_one.mainloop()