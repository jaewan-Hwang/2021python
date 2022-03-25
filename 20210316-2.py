money,a50000,a10000,a5000,a1000=0,0,0,0,0

money=int(input("지폐로 교환할 돈은 얼마?:"))



a50000=money//50000
money%=50000


a10000=money//10000
money%=10000

a5000=money//5000
money%=5000

a1000=money//1000
money%=1000


print("오만원짜리==>%d 장" % a50000)
print("만원짜리  ==>%d 장" % a10000)
print("오천원짜리==>%d 장" % a5000)
print("천원짜리  ==>%d 장" % a1000)
print("지폐로 바꾸지 못한 돈 ==> %d 원" %money)
          

