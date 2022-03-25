sum,i=0,0

for i in range(1,101,1):
    sum+=i
    if sum>500:
        break

print("1부터 100까지 합은 %d입니다." %sum)



print("합이 500보다 커지는 순간 i값은 %d입니다" %i)
