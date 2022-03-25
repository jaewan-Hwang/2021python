tt1=[]
tt2=[]
f=1


for i in range(0,3):
    for k in range(0,3):
        tt1.append(f)
        f+=1
    tt2.append(tuple(tt1))
    tt1=[]

    
for i in range(0,3):
    for k in range(0,3):    
        print("%3d" %tt2[i][k],end="")
    print("")


tt3=tuple(tt2)

print(tt3)

    
