from tkinter import*
from tkinter.simpledialog import*

#함수정의
window=Tk()
window.geometry("400x100")

label1=Label(window,text="입력된 값")
label1.pack()

value=askinteger("확대배수","주사위숫자(1~6)을 입력하세요",minvalue=1,maxvalue=6)

label1.configure(text=str(value))

window.mainloop()



