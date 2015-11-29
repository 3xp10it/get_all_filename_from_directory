import os
all=[]
os.system("ls *.py > 2.list")
f=open('2.list','r')
f1=open('3.list','w')
while True:
    line=f.readline()
    if line:
        out='\''+line.split('.')[0]+'\''+','
        print out,
        f1.write(out)
    else:
        break

