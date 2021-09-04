def change_time():
    origin_ = input("Number:")
    origin_min = origin_[0]
    origin_min = int(origin_min)
    origin_sec = origin_[3,4]
    origin_sec = int(origin_sec)
    min_ = origin_min * 60
    res_ = min_ + origin_sec
    print(res_)
change_time()
