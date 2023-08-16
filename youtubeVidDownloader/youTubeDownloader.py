#inthis project the pytube is used to download the video
from tkinter import *
from pytube import YouTube

m=Tk()
m.geometry("500x500")
m.title("YDownloader")

Label(m,text="Youtube video downloader",font="Consolas 15 bold").pack()

myvar=StringVar()
myvar.set("Enter the link below")
Entry(m,textvariable=myvar,width=40).pack()

def download():
    try:
        myvar.set("Downloading")
        m.update()
        YouTube(link.get()).streams.first().download()
        link.set("video downloaded successfully")

    except Exception as e:
        myvar.set("mistake")
        m.update()
        link.set("enter correct link")



link=StringVar()
link.set("Enter the link of a video to download")
Entry(m,textvariable=link,width=40).pack(pady=10)

Button(m,text="download",padx=10,bd=3,command=download).pack()

m.mainloop()
