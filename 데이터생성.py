import sqlite3

##변수
con,cursor=None,None
data1,data2,data3="","",""
sql=""

##메인
con=sqlite3.connect("medicineDB")
cur=con.cursor()

while (True):
    data1=input("약물이름==>:")
    if data1=="":
        break;
    data2=input("기능==>:")
    data3=input("성분==>:")

    sql="insert into colicTable values('"+data1+"','"+data2+"','"+data3+"')"
    cur.execute(sql)

con.commit()
con.close()


