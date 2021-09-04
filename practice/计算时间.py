import time

def deco (func):
    def get_time (*args):
        startTime = time.time()
        func (*args)
        endTime = time.time()
        print ("程序运行时间是{}秒".format (endTime - startTime))
    return get_time

@deco
def get_sum (n):
    sum = 0
    for i in range (1,n+1):
        sum += i
    print ("1到{}的正整数和是{}".format(n,sum))
