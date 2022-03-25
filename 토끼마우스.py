from tkinter import*
import tkinter.messagebox


##함수정의
def clickImage(event):
    tkinter.messagebox.showinfo("마우스","토끼에서 마우스가 클릭됨")

##메인코드
window=Tk()
window.geometry("400x400")
photo=PhotoImage(file="GIF/rabbit.gif")
label1=Label(window,image=photo)

label1.bind("<Button>",clickImage)

label1.pack(expand=1,anchor=CENTER)
window.mainloop()
