from tkinter import*
import tkinter.messagebox
window=Tk()


##함수정의
def myfunc():
    if chk.get()==0:
        tkinter.messagebox.showinfo("","체크버튼이 꺼졌네요.")
    else:
        tkinter.messagebox.showinfo("","체크버튼이 켜졌네요.")

#메인

chk= IntVar()
cb1=Checkbutton(window,text="클릭하세요",variable=chk,command=myfunc)


cb1.pack()


window.mainloop()
