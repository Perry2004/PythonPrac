import random
import tkinter as tk

window_one = tk.Tk()
window_one.title("图形版猜数字")
window_one.geometry('400x400')

def GuessNumber():
    label_range = tk.Label(window_one, text='请设置范围：')
    entry_range = tk.Entry(window_one)
    entry_answer = tk.Entry(window_one)
    button_submit_answer = tk.Button(window_one)

    label_answer = tk.Label(window_one, text='等待输入')

    def set_range(event):
        label_answer['text'] = '本程序随机生成了一个1-{}直接的整数，你猜是几：'.format(int(entry_range.get()))
    
    button_submit_range.bind('<Button-1>', set_range)
    y = random.randint(1,int(entry_range.get()))
    
    def parameter_list():
       
        pass set_answer(event):
        answer_ = int(entry_answer.get())

        global response_
        response_ = ''
        if y < answer_:
            response_ = ("猜大了哦，再来一次吧")
        elif y > answer_:
            response_ = ("猜小了哦，再来一次吧")
        elif y == answer_:
            response_ = "恭喜你猜对了。\r感谢使用，祝生活顺利

    label_response = tk.Label(window_one, text='答题结果{}'.format(response_) )
    button_submit_answer.bind('<Button-1>', set_answer)

    label_range.pack
    entry_range.pack
    button_submit_range.pack
    label_answer.pack
    entry_answer.pack
    button_submit_answer.pack
    label_response.pack

    window_one.mainloop()
GuessNumber()
