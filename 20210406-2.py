import random
gababo=[]
sa=0
a,b=0,0



for a in range(0,5,1): #컴터의 가위바위보
	gababo.append(random.randrange(0,3))


for b in range(0,5,1): #사람이 입력한 가위바위보 가위=0 바위=1 보=2
	sa=int(input("가위=0,바위=1,보=2 를 정해서 숫자로 입력하세요:")) 
	
	if (gababo[b]==sa):
		print("비겼습니다.")
	elif (gababo[b]<sa)  or (gababo[b]==2 and sa==0):
		print("이겼습니다.")
	else:
		print("졌습니다.")

print(gababo)##사용자가 컴퓨터가낸 결과랑 비교하기위하여 넣음
