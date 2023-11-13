from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


def home_page():
    gui_window.destroy()
    import GUI


def close_page():
    messagebox.showinfo('Face Recognition and Attendance System', 'Thankyou For Using Our Project !!')
    gui_window.destroy()


gui_window = Tk()
gui_window.geometry('1080x580')
gui_window.resizable(False, False)
gui_window.title('Face Recognition And Attendance System(Main Page)')

bgImage = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI main/code.jpg')

bgLabel = Label(gui_window, image=bgImage)
bgLabel.place(x=0, y=0)

ask2Button = Button(gui_window, text='Start The Project',  command=home_page,font=('times new roman', 24, 'bold'),bg='black', fg='white')
ask2Button.place(x=240, y=480)

askButton = Button(gui_window, text='Quit The Project',command=close_page, font=('times new roman', 24, 'bold'),bg='black', fg='white')
askButton.place(x=590, y=480)


gui_window.mainloop()