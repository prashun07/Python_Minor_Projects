#!/usr/bin/env python
# coding: utf-8




#importing Libraries
from tkinter import *
from pytube import YouTube
#Creating window
root=Tk()
root.geometry("500x300")
root.resizable(0,0)#set to fix window size
root.title("YouTube Video Downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

#Creating Field to enter link
link=StringVar()
Label(root,text="Enter Your Link",font='arial 15 bold').place(x=160,y=60)
link_enter=Entry(root,width=70,textvariable=link).place(x=32,y=90)

#function to download video
def Downloader():
    try:
        url=YouTube(str(link.get()))
        video=url.streams.first()
        video.download()
        Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
    except:
        Label(root,text='Invalid Link',font='arial 15').place(x=80,y=210)
        

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()







