def translate_():
    objects_ = input ("The object to be converted is:")
    for i in objects_:
        results_ = (ord(i))
        print (results_, end = "")
        if i != objects_[-1]:
            print(",", end = "")
    print ()
translate_()
