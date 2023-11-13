from tkinter import *
from PIL import ImageTk


def login_page():
    gui_window.destroy()
    import signIn


def signup_page():
    gui_window.destroy()
    import signup


gui_window = Tk()
gui_window.geometry('1080x580')
gui_window.resizable(False, False)
gui_window.title('Face Recognition And Attendance System')

bgImage = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI main/main gui.jpg')

bgLabel = Label(gui_window, image=bgImage)
bgLabel.place(x=0, y=0)

upPic = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI main/signup.jpg')
askButton = Button(gui_window, image=upPic, command=signup_page)
askButton.place(x=664, y=165)

inPic = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI main/login.jpg')
ask2Button = Button(gui_window, image=inPic, command=login_page)
ask2Button.place(x=664, y=300)

heading = Label(gui_window, text='---- Click Here To SignUp', font=('Times New Roman', 19, 'bold')
                , bg='white')
heading.place(x=774, y=185)

heading2 = Label(gui_window, text='---- Click Here To Login', font=('Times New Roman', 19, 'bold')
                , bg='white')
heading2.place(x=774, y=320)

gui_window.mainloop()
