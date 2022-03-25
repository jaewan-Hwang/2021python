from tkinter import*
window=Tk()

#함수정의

Photo=None


Photo1=PhotoImage(file="GIF/dog.gif")
Photo2=PhotoImage(file="GIF/cat.gif")
Photo3=PhotoImage(file="GIF/rabbit.gif")


def myfunc():
    if var.get()==1:
        label1.configure(image=Photo1)
    elif var.get()==2:
        label1.configure(image=Photo2)
    else:
        label1.configure(image=Photo3)



#메인코드
var=IntVar()


rb1=Radiobutton(window,text="강아지",variable=var,value=1,command=myfunc)

rb2=Radiobutton(window,text="고양이",variable=var,value=2,command=myfunc)

rb3=Radiobutton(window,text="토끼",variable=var,value=3,command=myfunc)

label1=Label(window, text="선택한 동물",fg="black")


label1.pack()
rb1.pack()
rb2.pack()
rb3.pack()


window.mainloop()
