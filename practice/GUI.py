import tkinter as tk    

window_one = tk.Tk()
window_one.title('Final and forever')
window_one.geometry('600x600')
label_one = tk.Label(window_one, text = 'Hello world', bg = 'red')  #创建标签并设置内容
label_one.pack()    #布局标签
window_one.mainloop()   #执行主事件循环
