import time

def deco (func):
    def get_time (*args):
        startTime = time.time()
        func (*args)
        endTime = time.time()
        print ("程序运行的时间是{}秒".format(endTime - startTime))
    return get_time