aa=[]
for i in range(0,4):
    aa.append(0)
hap=0

for i in range(0,41):
    aa[i]=int(input(str(i+1)+ "번째 숫자:"))
    hap=hap+aa[i]
print("합계==>%d" %hap)
'''
aa[0]=int(input("1번째 숫자:"))
aa[1]=int(input("2번째 숫자:"))
aa[2]=int(input("3번째 숫자:"))
aa[3]=int(input("4번째 숫자:"))
aa[4]=int(input("5번째 숫자:"))
aa[5]=int(input("6번째 숫자:"))
aa[6]=int(input("7번째 숫자:"))
aa[7]=int(input("8번째 숫자:"))



hap=aa[0]+aa[1]+aa[2]+aa[3]+aa[4]+aa[5]+aa[6]+aa[7]

print("합계==>%d" %hap)

'''
