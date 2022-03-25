from tkinter import*
import tkinter.messagebox
#함수정의

def clickMouse(event):
    txt=""
    if event.num==1:
        txt+="마우스 왼쪽 버튼이("
    elif event.num==3:
        txt+="마우스 오른쪽 버튼이("

    txt+=str(event.x)+","+str(event.y)+")에서 클릭됨"
    label1.configure(text=txt)

def keyEvent(event):
    tkinter.messagebox.showinfo("키보드 이벤트","눌린키:"+chr(event.keycode))

##메인
window=Tk()
window.geometry("400x400")

label1=Label(window,text="이곳이 바뀜")
window.bind("<Button>",clickMouse)


window.bind("<Key>",keyEvent)

label1.pack(expand=1,anchor=CENTER)
window.mainloop()
