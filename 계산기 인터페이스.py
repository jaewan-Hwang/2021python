from tkinter import*

#변수

btnList=[None]*16
xPos,yPos=0,70
i,k=0,0
num=0

#메인
window=Tk()
window.geometry("280x350")

label2=Label(window,text=str(num),anchor=SE,font=(50))
label2.place(width=280,height=70,x=0,y=0)


for i in range(0,16):
    btnList[i]=Button(window,text=str(i))

for i in range(0,4):
    for k in range(0,4):
        btnList[num].place(width=70,height=70,x=xPos, y=yPos)
        num+=1
        xPos+=70
    xPos=0
    yPos+=70

window.mainloop()

