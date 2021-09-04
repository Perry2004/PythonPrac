from multiprocessing import Process

def sub(i):
    print('子进程{}已启动'.format(i))

def main():
    print('主进程启动')
    for i in range(100*100):
        pro = Process (target=sub, args=(i,))
        pro.start()

if __name__ == "__main__":
    main()