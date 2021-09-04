def switch_back():
    global ASCII_
    ASCII_ = input ("The object to be switched back is:")
    ASCII_ = ASCII_.strip()
    for i in ASCII_:
        ASCII_ = list (ASCII_)
        print (chr(int(i)),end = "")
switch_back()
