from tkinter import*
import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    
root = Tk()
root.title("text to speech")
root.geometry("400x200")
root.resizable(False,False)

textv = StringVar()

obj =LabelFrame(root,text="text to speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl = Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)

text = Entry(obj,textvariable=textv,font=30,bd=1)
text.pack(side=tk.LEFT,padx=5)

btn = Button(obj,text="Speak",font=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)



root.mainloop()