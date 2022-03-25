from tkinter import*

window=Tk()
label0=Label(window, text="안녕하세요 저는 황재입니다.",font=("고딕체",30))
photo1=PhotoImage(file="GIF/cat.gif")
label1=Label(window, image=photo1)
photo2=PhotoImage(file="GIF/jeju11.gif")
label2=Label(window, image=photo2)
button1=Button(window, text="파이썬 종료", fg="red", command=quit)




##이 부분에서 화면을 구성하고 처리


label0.pack()
label1.pack()
label2.pack()
button1.pack()

window.mainloop()

