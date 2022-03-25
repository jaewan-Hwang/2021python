from tkinter import*
import tkinter.messagebox
window=Tk()


##함수정의
def myfunc():
    if chk1.get()==1 and chk2.get()==0:
        tkinter.messagebox.showinfo("","파이썬")
    elif chk1.get()==0 and chk2.get()==1:
        tkinter.messagebox.showinfo("","자바")
    elif chk1.get()==1 and chk2.get()==1:
        tkinter.messagebox.showinfo("","둘다선택")
    else:
        tkinter.messagebox.showinfo("","아무것도 선택안함")
        
        

#메인

chk1= IntVar()
cb1=Checkbutton(window,text="파이썬",variable=chk1)
chk2= IntVar()
cb2=Checkbutton(window,text="자바",variable=chk2)

button1=Button(window,text="누르세요",command=myfunc)


cb1.pack()
cb2.pack()
button1.pack()
window.mainloop()
