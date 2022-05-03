from tkinter import *
import time
import random

root = Tk()
root.title("Guess the Number Game")
root.geometry("500x350")

topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

def incorrectbutton():
  yes.pack_forget()
  no.pack_forget()
  damnit = Label(topframe, text="Damn! I got it wrong!")
  damnit.pack()
  exitbutton.pack()

def correctbutton():
  no.pack_forget()
  yes.pack_forget()
  letsgo = Label(bottomframe, text="lets go! I got it right!")
  letsgo.pack()
  exitbutton.pack()

def guessingnow():
  guessed2()

yes = Button(topframe, text="Yes", bg="green", fg="black", command=correctbutton)
no = Button(topframe, text="No", bg="red", fg="black", command=incorrectbutton)

def yesorno():
  yes.pack(side=LEFT)
  no.pack(side=RIGHT)

def exitbutton():
  root.destroy()

def guessed2():
  guess = random.randint(1,10)
  answer = Label(bottomframe, text=(guess))
  answer.pack(side=BOTTOM)
  yesorno()

def clickyesButton():
  yesbutton.pack_forget()
  explanation.pack_forget()
  time.sleep(1)
  guessingnow()

yesbutton = Button(bottomframe, text="I've thought of one", bg="black", fg="white", command=clickyesButton)
yesbutton.pack(side=LEFT)

exitbutton = Button(root, text="exit", fg="black", command=exitbutton)

explanation = Label(topframe, text="Think of a number between 1 and 10", fg="red" )
explanation.pack(side=BOTTOM)

root.mainloop()

