import random

##함수정의부분
def getNumber():
    return random.randrange(1,46)

##변수선언부분
lotto=[]
num=0


##메인코드부분
print("**로또 추첨을 시작합니다.**\n");

while True:
    num=getNumber()

    if lotto.count(num)==0:
        lotto.append(num)
        



    if len(lotto)>= 6:
        break



print("추첨된 로또번호==>",end='')
lotto.sort()
for i in range (0,6):
    print("%d "%lotto[i],end='')


