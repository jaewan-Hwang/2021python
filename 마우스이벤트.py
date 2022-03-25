from tkinter import*
import tkinter.messagebox

##함수정의
def clickLeft(event):
    tkinter.messagebox.showinfo("마우스","마우스 왼쪽 버튼이 클릭됨")

##메인코드
window=Tk()

window.bind("<Button-1>",clickLeft)

window.mainloop()
