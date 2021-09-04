a=1
b=2
c=3

f=open('test.txt','a')
print(a,b,c,sep='......',end='?',file=f)
f.close()
