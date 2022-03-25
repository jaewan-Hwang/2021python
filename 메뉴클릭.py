from tkinter import*
import tkinter.messagebox


#함수정의
def func_open():
    tkinter.messagebox.showinfo("메뉴선택","열기메뉴를 선택함")
    
def func_exit():
    window.quit()
    window.destroy()

#메인
        
window=Tk()


mainMenu=Menu(window)
window.config(menu=mainMenu)

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=fileMenu)
fileMenu.add_command(label="열기",command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="저장")
fileMenu.add_separator()
fileMenu.add_command(label="종료",command=func_exit)
