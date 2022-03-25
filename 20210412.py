##변수선언부분
parking=[]
top,carName,outCar=0,"A",""
select=9

##메인코드
while(select!=3):
    select=int(input("<1>자동차넣기<2>자동차빼기<3>끝:"))

    if(select==1):
        if(top>=5):
            print("주차장이 꽉 차서못들어감")
        else:
            parking.append(carName)
            print("%s 자동차들어감.주차장상태==>%s " %(parking[top],parking))
            top+=1
            carName=chr(ord(carName)+1)

    elif(select==2):
        if(top<=0):
            print("빠져나갈 자동차가 없음")
        else:
            outCar=parking.pop()
            print("%s 자동차들어감.주차장상태==>%s " %(outCar,parking))
            top-=1
            carName=chr(ord(carName)-1)

    elif(select==3):
        break;
    else:
        print("잘못 입력했네요. 다시입력하세요.")

print("현재 주차장에 %d대가 있음" %top)
print("프로그램을 종료합니다.")



    
