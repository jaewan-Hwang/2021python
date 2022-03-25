##함수선언 

def func():
    global X
    X=10
    #지역변수이지만 global함수를 선언하여
    #전역변수로 바뀜. 하지만 위치는 지역변수위치 
    
    print (X)
    
func()
