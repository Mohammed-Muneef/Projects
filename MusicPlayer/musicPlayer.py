from tkinter import *
from pygame import mixer

m=Tk()

m.geometry("500x500")

mixer.init()
mixer.music.load("filename.mp3")

def play():
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

Label(m,text="Music player").pack()
Button(m,text="play",command=play).place(x=150,y=100)
Button(m,text="pause",command=pause).place(x=200,y=100)
Button(m,text="resume",command=resume).place(x=250,y=100)
Button(m,text="quit",command=quit).place(x=320,y=100)
m.mainloop()