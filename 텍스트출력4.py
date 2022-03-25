inFp=None#입력파일
inStr=""#읽어온 문자열

inFp=open("C:/temp/data1.txt","r",encoding="utf-8")

inList=inFp.readlines()
for inStr in inList:
    print(inStr,end='')


inFp.close()
