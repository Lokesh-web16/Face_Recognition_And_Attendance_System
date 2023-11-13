import tkinter
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition
import threading


def home_page():
    root.destroy()
    import GUI2


bot = ChatBot('Naruto')
trainer = ListTrainer(bot)
for files in os.listdir('data/About Project/'):
    data = open('data/About Project/'+files, 'r', encoding='utf-8').readlines()

    trainer.train(data)


def botReply():
    question = questionField.get()
    question = question.capitalize()
    answer = bot.get_response(question)
    textarea.insert(END, 'You: ' + question + '\n\n')
    textarea.insert(END, 'Naruto: ' + str(answer) + '\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0, END)


def audioToText():
    while True:
        sr = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as m:
                sr.adjust_for_ambient_noise(m, duration=0.8)
                audio = sr.listen(m)
                query = sr.recognize_google(audio)

                questionField.delete(0, END)
                questionField.insert(0, query)
                botReply()

        except Exception as e:
            print(e)


root = tkinter.Tk()


root.geometry('500x570+100+30')
root.title('Naruto Uzumaki Chatbox')
root.config(bg='medium sea green')

logoPic = PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/Talking Chatbox/naruto.png')

logoPicLabel = Label(root, image=logoPic, bg='black')
logoPicLabel.pack()

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame, font=('times new roman', 20, 'bold'), height=10, yscrollcommand=scrollbar.set
                , wrap='word', bg='black', fg='white')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField = Entry(root, font=('verdana', 20, 'bold'))
questionField.pack(pady=15)

askPic = PhotoImage(file='C:/Users/Lokesh T/PycharmProject/face/Talking Chatbox/logobot.png')
askButton = Button(root, text='Ask Naruto Bot', font=('times new roman', 14, 'bold'), command=botReply)
askButton.place(x=90,y=520)

askButton2 = Button(root, text='Return To Home', font=('times new roman', 14, 'bold'), command=home_page)
askButton2.place(x=250,y=520)


def click(event):
    askButton.invoke()


root.bind('<Return>', click)

thread = threading.Thread(target=audioToText)
thread.daemon = True
thread.start()

root.mainloop()
