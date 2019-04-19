import json
from difflib import get_close_matches
from tkinter import *
import tkinter.messagebox


root = Tk()
root.title("dictionary")

root.config(background="silver")
file = open("data_dict.json","r")
data = json.load(file)
frame = Frame(root)
frame.grid(row = 2,column=0)

def meaning():
    w = (str(e1.get())).lower()
    if w in data:
        for i in range(len(data[w])):
            text1.insert(END,w+" : "+str(data[w][i])+"\n")
    elif len(get_close_matches(w,data.keys())) > 0:
        tkinter.messagebox.showinfo("404","This word is not present in our lexicon showing results for %s instead"% get_close_matches(w,data.keys())[0])
        for i in range(len(data[get_close_matches(w,data.keys())[0]])):
            text1.insert(END,str(get_close_matches(w,data.keys())[0])+" : "+str(data[get_close_matches(w,data.keys())[0]][i])+"\n")
    else:
        tkinter.messagebox.showinfo("404","This word is not present in our lexicon\nDouble check it.")

l0 = Label(root,text="DICTIONARY")
l0.grid(row = 0)
l0.config(font=("Courier", 44),fg="#191970")
l1 = Label(root,text="Enter word").grid(row = 1)
l2 = Label(root,text="Meaning").grid(row = 4)

sb = Scrollbar(root)
sb.grid(row=5,column=3)

text1 = Text(root, height=20, width=60,yscrollcommand=sb.set,font=("Courier", 16))
text1.grid(row = 5)

sb.config(command=text1.yview)

e1 = Entry(root)
e1.grid(row = 1)
e1.focus()

b1 = Button(frame,text = "Search",command = meaning,bg="#F0F8FF",fg = "#00008B",bd =7, cursor ="sailboat")
b1.grid(row = 3,column = 0)

root.mainloop()
