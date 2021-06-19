from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.title('Data Flair-Text to Speech')
root.configure(bg='ghost white')
root.geometry('350x350')
Label(root, font='arial 15 bold', text='Text to Speech', bg='white smoke').pack()
Label(root, text='data Flair', bg='white smoke', font='arial 15 bold', width='20').pack(side='bottom')

msg = StringVar()
Label(root, text='Enter text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)
entry_field = Entry(root, textvariable=msg, width='50')
entry_field.place(x=20, y=100)


def Text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')


def reset():
    msg.set('')


def exit():
    root.destroy()


Button(root, text='Play', font='arial 15 bold', command=Text_to_speech, width='4').place(x=25, y=140)
Button(root, text='Exit', font='arial 15 bold', command=exit, width='4').place(x=100, y=140)
Button(root, text='Reset', font='arial 15 bold', command=reset, width='4').place(x=175, y=140)

root.mainloop()
