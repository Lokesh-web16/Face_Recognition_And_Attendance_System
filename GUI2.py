from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


def face_rec():
    import main


def chat_bot():
    messagebox.showinfo('Chat box', 'Please wait Our Chatbox is loading....')
    gui_window.destroy()
    import main2


def camera_cap():
    import CaptureImage


def data_base():
    messagebox.showinfo('Add to Database', 'Please wait Face Data is Being Saved !')
    import AddDataToDatabase


def encode_gen():
    messagebox.showinfo('Encode Generator', 'Please wait Face Data Encoding Started')
    import EncodeGenerator


def emotion():
    messagebox.showinfo('Emotion Detection', 'Please wait for 30 Seconds , Loading....')
    import realtimedetection


def logout():
    gui_window.destroy()
    import signIn


gui_window = Tk()
gui_window.geometry('1080x580')
gui_window.resizable(False, False)
gui_window.title('Face Recognition And Attendance System')

bgImage = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI main/main2.jpg')

bgLabel = Label(gui_window, image=bgImage)
bgLabel.place(x=0, y=0)

facerec = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI 2/facerec.jpg')
askButton1 = Button(gui_window, image=facerec, background='black', command=face_rec)
askButton1.place(x=700, y=165)

newface = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI 2/capture.jpg')
askButton2 = Button(gui_window, image=newface, background='black', command=camera_cap)
askButton2.place(x=700, y=310)

signup = ImageTk.PhotoImage(file='Resources/sample24.png')
askButton3 = Button(gui_window, image=signup, background='black', command=emotion)
askButton3.place(x=700, y=445)

chat = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI 2/chatbot.jpg')
askButton4 = Button(gui_window, image=chat, background='black', command=chat_bot)
askButton4.place(x=915, y=165)

data = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI 2/database.jpg')
askButton5 = Button(gui_window, image=data, background='black', command=data_base)
askButton5.place(x=915, y=310)

encode = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/GUI 2/encode.jpg')
askButton6 = Button(gui_window, image=encode, background='black', command=encode_gen)
askButton6.place(x=915, y=445)

heading1 = Label(gui_window, text='Face Recognition & Attendance', font=('Times New Roman', 10, 'bold')
                , bg='red', fg='white')
heading1.place(x=666, y=254)

heading2 = Label(gui_window, text='Talk To Chatbot - FAQ', font=('Times New Roman', 10, 'bold')
                , bg='red', fg='white')
heading2.place(x=904, y=254)

heading3 = Label(gui_window, text='Open Camera & Capture New Face', font=('Times New Roman', 10, 'bold')
                , bg='red', fg='white')
heading3.place(x=656, y=400)

heading4 = Label(gui_window, text='Real-Time Face Emotion Detection', font=('Times New Roman', 10, 'bold')
                , bg='red', fg='white')
heading4.place(x=654, y=534)

heading5 = Label(gui_window, text='Add Face To Database - Firebase', font=('Times New Roman', 10, 'bold')
                , bg='red', fg='white')
heading5.place(x=880, y=400)

heading6 = Label(gui_window, text='Start Face Encode Generator', font=('Times New Roman', 10, 'bold')
                , bg='red', fg='white')
heading6.place(x=886, y=534)

Logout = Button(gui_window, text='Log Out !!', font=('Times New Roman', 16, 'bold'), bd=0, bg='red',fg='white'
                      , activeforeground='white', activebackground='red', command=logout)
Logout.place(x=517, y=488)

gui_window.mainloop()
