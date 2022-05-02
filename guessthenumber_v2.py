from tkinter import *
import random
import sys
import os

root = Tk()
root.title("Guess the Number Game")
root.geometry("500x350")

titleframe = Frame(root)
titleframe.configure(bg="grey")
titleframe.pack()

upperframe1 = Frame(root)
upperframe1.pack()

upperframe2 = Frame(root)
upperframe2.pack()

middleframe1 = Frame(root)
middleframe1.pack()

middleframe2 = Frame(root)
middleframe2.pack()

lowerframe1 = Frame(root)
lowerframe1.pack()

lowerframe2 = Frame(root)
lowerframe2.pack()

nameframe = Frame(root)
nameframe.pack()

copyrightnameline = Label(nameframe, text="©TSM Software Development 2022", font="Courier 4")
copyrightnameline.pack()

titlelinetext = Label(titleframe, text="""Guess the Number Game
""", fg="purple", font="Montserrat 28 bold")
titlelinetext.pack()

def exit():
    root.destroy()

exitbutton = Button(lowerframe2, text="Exit", fg="Purple", bg="Grey", font="Montserrat 16", command=exit)


def correctbuttonfunc():
    upperframe2.pack_forget()
    lowerframe1.pack_forget()
    correctlabel = Label(middleframe2, text="Yes! I got it right!", fg="Purple", font="Montserrat 14")
    correctlabel.pack()
    exitbutton.pack()



def incorrectbuttonfunc():
    upperframe2.pack_forget()
    lowerframe1.pack_forget()
    incorrectlabel = Label(middleframe2, text="No! I lost!", fg="Purple", font="Montserrat 14")
    incorrectlabel.pack()
    exitbutton.pack()

def randomfunc():
    computerguess = random.randint(1,10)
    guesslabel = Label(upperframe2, text=(f"My guess is {computerguess}"), fg="Purple", font="Montserrat 16")
    guesslabel.pack()
    correctbutton = Button(lowerframe1, text="Yes", fg="Yellow", bg="Grey", font="Helvetica 14", command=correctbuttonfunc)
    correctbutton.pack(side=LEFT)
    spacer1label = Label(lowerframe1, text="              or                ", fg="Purple")
    spacer1label.pack(side=LEFT)
    incorrectbutton = Button(lowerframe1, text="No", fg="Yellow", bg="Grey", font="Helvetica 14", command=incorrectbuttonfunc)
    incorrectbutton.pack(side=RIGHT)

def guessmynumfunc():
    middleframe1.pack_forget()
    upperframe1.pack_forget()
    randomfunc()


def maingame_root():
    instruction1 = Label(upperframe1, text="""Think of a number between
    1 and 10
    """, font="Montserrat 18")
    instruction1.pack()
    guessmynumbutt = Button(middleframe1, text="Guess my number", fg="Yellow", bg="Grey", font="Montserrat 14", command=guessmynumfunc)
    guessmynumbutt.pack()



def startgamecommand():
    startgamebutton.pack_forget()
    maingame_root()


startgamebutton = Button(lowerframe1, text="Start", fg="yellow", bg="grey", font="Monstserrat 28",  command=startgamecommand)
startgamebutton.pack()


root.mainloop()