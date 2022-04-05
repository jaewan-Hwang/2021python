#날짜 연 월 일을 입력하면 10년후의 날짜를 출력합니다.
ss=input("날짜(연/원/일) 입력==>")


ssList=ss.split('/')


print("입력한 날짜의 10년후==>", end='')
print(str(int(ssList[0])+10)+"년",end='')
print(ssList[1]+"월",end='')
print(ssList[2]+"일")

