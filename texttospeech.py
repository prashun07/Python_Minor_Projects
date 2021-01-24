# -*- coding: utf-8 -*-
"""

@author: Prashun
"""
"""importing required Libraries"""

from tkinter import * #python library to build GUI
from gtts import gTTS #Python library to convert text into audio
from playsound import playsound #Python module to play audio sound file
import os

"""Initializing window"""
root=Tk() #To initialize tkinter to create GUI
root.geometry("350x300") #geometry() used to set height & width
root.configure(bg="ghost white")#used to access window attributes,bg used for background
root.title("TEXT TO SPEECH") #title used to set title

#Label() is widget is used to display one or more than one line of text that 
#users can’t able to modify.

Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
#root is the name which we refer to window
#text which is used to display on our label
#font on which text is written
#pack organised widget in block
Label(text ="Prashun Kumar", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar() #Msg is a string type variable

Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable = Msg ,width ='50')
#Entry used to create input text field
#textvariable used to get  current text to widget
entry_field.place(x=20,y=100) #place organise widget in specific position

"""Function to convert text to speech"""

def Text_to_speech():
    Message=entry_field.get()#message store value of entry field
    speech=gTTS(text=Message)#passing message into gtts 
    #default language above is English otherwise we will use *lang*
    #speech save voice converted from text
    #to read slowly we can use slow(),default is false
    speech.save("E:/textspeech.mp3")#save() used to save in req. mp3 format
    playsound("E:/textspeech.mp3")#used to play saved file
    
#Function to exit
def Exit():
    root.destroy()#it quit the program by stopping mainloop
    
#Function to reset
def Reset():
    Msg.set("")#Reset function set Msg variable to empty string
    
#Create Button to play audio
#Button widget is used to create button on window
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)
    
root.mainloop()#it execute when we run our program

    



