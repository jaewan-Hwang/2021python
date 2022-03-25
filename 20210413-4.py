##변수

an={'닭':'병아리',
       '개':'강아지',
       '곰':'능소니',
       '고등어':'고도리',
       '명태':'노가리',
       '말':'망아지',
       '호랑이':'개호주',};

##메인
print(str(an.keys()))
print(str(an.values()))

while(True):
    ban=input(str(list(an.keys()))+"중 새끼 이름을 알고 싶은 동물?")
    if ban in an:
        print('<%s>의 새끼는<%s>입니다.' %(ban,an.get(ban)))
    elif ban=='끝':
        break
    else:
        print("그 동물의 새끼이름은 모르겠네요. 확인해보세요.")
