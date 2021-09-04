x = 0
y = 0
for i in range(0,9):
    for j in range (0,9):
        if (50 + x) * 4158 == (10 * y + 3) * 3564:
            print ("The answer is, x is",(x),",","y is",(y))
            break
        else:
            y += 1
    y = 0
    x += 1
print ("Finish")