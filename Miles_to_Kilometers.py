from tkinter import *

#My Code

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=275,height=100)


def clicked():
    mile = input.get()
    km = float(mile) *1.60934
    labelk.config(text=f"{km}")

input = Entry(width=10)
input.grid(column=1, row = 0)

label = Label(text="miles")
label.grid(column=2, row = 0)
#label.pack(side="left")

labelj = Label(text="is equal to")
labelj.grid(column = 0, row = 1)

labelk = Label(text="0")
labelk.grid(column=1, row=1)

labell = Label(text="kilometers")
labell.grid(column=2, row=1)

button = Button(text="convert", command= clicked)
button.grid(column =1, row=2)
#button.pack()

window.mainloop()

#Udemy Way















