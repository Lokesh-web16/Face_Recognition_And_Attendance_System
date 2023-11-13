from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def forgot_password():
    def change_password():
        if usernameEntry1.get()=='' or usernameEntry2.get()=='' or usernameEntry3.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif usernameEntry2.get() != usernameEntry3.get():
            messagebox.showerror('Error', 'Password and Confirm Password Mismatch', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='1234',database='facedata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (usernameEntry1.get()))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query,(usernameEntry2.get(),usernameEntry3.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password Is Reset, Please login with New Details',parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change Password')
    window.resizable(False, False)
    background = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/SignIn/bg2.jpg')
    bgLabel2 = Label(window, image=background)
    bgLabel2.grid()

    reset = Label(window, text='RESET PASSWORD', font=('Times New Roman', 18, 'bold underline')
                    , bg='white')
    reset.place(x=602, y=100)

    name = Label(window, text='Username :', font=('Times New Roman', 15, 'bold')
                    , bg='white', fg='red')
    name.place(x=564, y=150)

    usernameEntry1 = Entry(window, width=30, font=('Times New Roman', 13, 'bold')
                          , bd=0, fg='black', bg='white')
    usernameEntry1.place(x=578, y=180)

    Frame(window, width=250, height=4, bg='black').place(x=572, y=199)

    name1 = Label(window, text='Password :', font=('Times New Roman', 15, 'bold')
                 , bg='white', fg='red')
    name1.place(x=564, y=220)

    usernameEntry2 = Entry(window, width=30, font=('Times New Roman', 13, 'bold')
                           , bd=0, fg='black', bg='white')
    usernameEntry2.place(x=578, y=250)

    Frame(window, width=250, height=4, bg='black').place(x=572, y=269)

    name2 = Label(window, text='Confirm Password :', font=('Times New Roman', 15, 'bold')
                  , bg='white', fg='red')
    name2.place(x=564, y=290)

    usernameEntry3 = Entry(window, width=30, font=('Times New Roman', 13, 'bold')
                           , bd=0, fg='black', bg='white')
    usernameEntry3.place(x=578, y=320)

    Frame(window, width=250, height=4, bg='black').place(x=572, y=339)

    forgButton = Button(window, text='Change Password', font=('Times New Roman', 16, 'bold')
                         , fg='white', bg='green', activeforeground='white'
                         , activebackground='red', cursor='hand2', bd=0, width=19,command=change_password)
    forgButton.place(x=590, y=370)

    window.mainloop()


def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
           con = pymysql.connect(host='localhost', user='root', password='1234')
           mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection Not Established,Try Again')
            return
        query = 'use facedata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row is None:
            messagebox.showerror('Error','Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome', 'Your Login is Successful')
            login_window.destroy()
            import GUI2


def signup_page():
    login_window.destroy()
    import signup


def hide():
    openeye.config(file='C:/Users/Lokesh T/PycharmProject/face/SignIn/openeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='C:/Users/Lokesh T/PycharmProject/face/SignIn/closeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def exit_web():
    login_window.destroy()
    import GUI


login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('FACE ATTENDANCE SYSTEM LOGIN')
bgImage = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/SignIn/bg.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Times New Roman', 23, 'bold underline')
                , bg='white')
heading.place(x=610, y=109)

usernameEntry = Entry(login_window, width=25, font=('Times New Roman', 11, 'bold')
                      , bd=0, fg='black')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=250, height=2, bg='black')
frame1.place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Times New Roman', 11, 'bold')
                      , bd=0, fg='black')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)
frame2 = Frame(login_window, width=250, height=2, bg='black')
frame2.place(x=580, y=282)

openeye = PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/SignIn/openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white'
                   , cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white'
                   , cursor='hand2', font=('Times New Roman', 11, 'bold'), command=forgot_password)
forgetButton.place(x=715, y=295)

loginButton = Button(login_window, text='Login Here', font=('Times New Roman', 16, 'bold')
                     , fg='white', bg='red', activeforeground='white'
                     , activebackground='red', cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=590, y=325)

orLabel = Label(login_window, text='---------------OR---------------', font=('Times New Roman', 16), fg='firebrick1', bg='white')
orLabel.place(x=585, y=385)

facebook_logo = PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/SignIn/facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640, y=420)

google_logo = PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/SignIn/google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690, y=420)

twitter_logo = PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/SignIn/twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740, y=420)

lineLabel = Label(login_window, text='--------------------------------------', font=('Times New Roman', 16), fg='black', bg='white')
lineLabel.place(x=570, y=458)

signupLabel = Label(login_window, text='Do not have an Account?', font=('Times New Roman', 12, 'bold'), fg='black', bg='white')
signupLabel.place(x=575, y=490)

newaccountButton = Button(login_window, text='Create New One', font=('Times New Roman', 9, 'bold underline')
                     , fg='blue', bg='white', activeforeground='blue'
                     , activebackground='white', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=750, y=493)


exitButton = Button(login_window, text='Return To Home', font=('Times New Roman', 16, 'bold')
                     , fg='white', bg='red', activeforeground='white'
                     , activebackground='red', cursor='hand2', bd=0, width=19, command=exit_web)
exitButton.place(x=230, y=520)

login_window.mainloop()
