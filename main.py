from tkinter import *

from datetime import date
window = Tk()
window.title("Sample Window")
window.geometry("400x400")
a = Label(text= "Hello every one", fg= "green", bg="black", height=1, width= 300)
n = Label(text= "name", bg= "blue")
n_entry = Entry()
def display():
    name= n_entry.get()
    global Message
    Message= "welcome to the application\ntodays date is: "
    great= "Hello"+ name + "\n"
    text_box.insert(END, great)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())
text_box = Text(height= 3)
btn = Button(text= "Begain", command= display, height=1, bg= "green", fg= "red")
a.pack()
n.pack()
n_entry.pack()
text_box.pack()
btn.pack()
window.mainloop()