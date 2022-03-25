outFp=None
outStr=""

outFp=open("c:/temp/data3.txt","w",encoding='utf-8')

while True:
    outStr=input("내용입력: ")
    if outStr !="":
        outFp.writelines(outStr+"\n")
    else:
        break

outFp.close()
print("-----정상적으로 파일에 써졌습니다--")
