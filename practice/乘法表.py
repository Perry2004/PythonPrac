for i in range (1,9):
    for j in range (1,9):
        if j<= i:
            print ("{}*{}={}".format (j,i,i*j),end = '\t')
    print ()