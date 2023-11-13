from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)


def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')
    else:
        try:
           con = pymysql.connect(host='localhost', user='root', password='1234')
           mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue,Please Try Again')
            return
        try:
            query = 'create database facedata'
            mycursor.execute(query)
            query = 'use facedata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use facedata')
        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error', 'Username Already Exists')

        else:
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration Successful')
            clear()


def login_page():
    signup_window.destroy()
    import signIn


def home_page():
    signup_window.destroy()
    import GUI


signup_window = Tk()
signup_window.title('User Signup Page')
signup_window.resizable(False, False)
background = ImageTk.PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/SignIn/bg2.jpg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window, bg='white')
frame.place(x=553, y=100)

heading = Label(frame, text='CREATE NEW ACCOUNT', font=('Times New Roman', 18, 'bold underline')
                , bg='white')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text='Email', font=('Times New Roman', 10, 'bold')
                   , bg='white', fg='red')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

emailEntry = Entry(frame, width=25, font=('Times New Roman', 15, 'bold')
                   , fg='white', bg='red')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Username', font=('Times New Roman', 10, 'bold')
                      , bg='white', fg='red')

usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, width=25, font=('Times New Roman', 15, 'bold')
                   , fg='white', bg='red')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text='Password', font=('Times New Roman', 10, 'bold')
                      , bg='white', fg='red')

passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = Entry(frame, width=25, font=('Times New Roman', 15, 'bold')
                   , fg='white', bg='red')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmLabel = Label(frame, text='Confirm Password', font=('Times New Roman', 10, 'bold')
                      , bg='white', fg='red')

confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

confirmEntry = Entry(frame, width=25, font=('Times New Roman', 15, 'bold')
                   , fg='white', bg='red')
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

check = IntVar()

termsandconditions = Checkbutton(frame, text='I agree to the Terms and Conditions', font=('Times New Roman', 10, 'bold')
                                 , bg='white', activebackground='white', cursor='hand2', variable=check)
termsandconditions.grid(row=9, column=0, padx=15, pady=10)

signupButton = Button(frame, text='Horray!! SignUp', font=('Times New Roman', 16, 'bold'), bd=0, bg='red', fg='white'
                      , activeforeground='white', activebackground='red', command=connect_database)
signupButton.grid(row=10, column=0)

alreadyaccount = Label(frame, text='You have an account?', font=('Times New Roman', 11, 'bold')
                       , bg='white', fg='red')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

LoginButton = Button(frame, text='Log In Here', font=('Times New Roman', 11, 'bold underline')
                     , fg='blue', bg='white', activeforeground='blue'
                     , activebackground='white', cursor='hand2', bd=0, command=login_page)
LoginButton.place(x=180, y=376)

HomeButton = Button(signup_window, text='Return Home', font=('Times New Roman', 16, 'bold'), bd=0, bg='red',fg='white'
                      , activeforeground='white', activebackground='red', command=home_page)
HomeButton.place(x=270, y=510)

signup_window.mainloop()