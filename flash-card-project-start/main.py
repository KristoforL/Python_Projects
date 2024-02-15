from tkinter import *
from tkinter import messagebox
from random import *
from pandas import *

current_card = {}
BACKGROUND_COLOR = "#B1DDC6"
learn = {}



# ----------------------------CARD FUNCTIONS ------------------------------- #
##Check button and wrong button 
try:
    # data = pandas.read_csv("/Users/kris/Desktop/Github/100daysOfCode/Day 31/flash-card-project-start/data/words to learn.csv")
    data = pandas.read_csv("E:/Github/100daysOfCode/Day 31/flash-card-project-start/data/words to learn.csv")
except FileNotFoundError:
    # data = pandas.read_csv("/Users/kris/Desktop/Github/100daysOfCode/Day 31/flash-card-project-start/data/french_words.csv")
    data = pandas.read_csv("E:/Github/100daysOfCode/Day 31/flash-card-project-start/data/french_words.csv")   
    learn  = data.to_dict(orient = "records")
else:
    learn = data.to_dict(orient = "records") 

words=data.to_dict(orient="records")


def flip():
    global current_card
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(img, image = back_img)
    canvas.itemconfig(ctitle, text = "English", fill = "white")
    canvas.itemconfig(cword, text= current_card["English"], fill = "white")

    



def next_card():
    global current_card
    
    canvas.itemconfig(img, image = front_img)
    current_card = choice(words)
    canvas.itemconfig(ctitle, text = "French", fill = "black")
    canvas.itemconfig(cword, text= current_card["French"], fill = "black")
    
    global timer
    timer = window.after(3000, func=flip)

def is_known():
    global current_card
    global timer
    window.after_cancel(timer)
    words.remove(current_card)
    print(len(words))
    # data = pandas.DataFrame(words)
    # data.to_csv("/Users/kris/Desktop/Github/100daysOfCode/Day 31/flash-card-project-start/data/words to learn.csv", index = False)
    
    data = pandas.DataFrame(words)
    data.to_csv("E:/Github/100daysOfCode/Day 31/flash-card-project-start/data/words to learn.csv")
    next_card()




# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.minsize()
window.title("Flashcards")
window.config(padx =50, pady = 50, bg = BACKGROUND_COLOR)

canvas = Canvas(height = 526, width =800, highlightthickness=0)

# front_img = PhotoImage(file="/Users/kris/Desktop/Github/100daysOfCode/Day 31/flash-card-project-start/images/card_front.png")
# back_img = PhotoImage(file="/Users/kris/Desktop/Github/100daysOfCode/Day 31/flash-card-project-start/images/card_back.png")
front_img = PhotoImage(file="E:/Github/100daysOfCode/Day 31/flash-card-project-start/images/card_front.png")
back_img = PhotoImage(file="E:/Github/100daysOfCode\Day 31/flash-card-project-start/images/card_back.png")
img = canvas.create_image(400,263,image=front_img)
canvas.config(bg=BACKGROUND_COLOR)
ctitle= canvas.create_text(400, 150, text = "", font = ("Ariel",40, "italic"))

cword = canvas.create_text(400, 263, text = "", font = ("Ariel",60, "bold"))

canvas.grid(row = 0, column =0, columnspan =2)



# check = PhotoImage(file = "/Users/kris/Desktop/Github/100daysOfCode/Day 31/flash-card-project-start/images/right.png")
# x_button = PhotoImage(file = "/Users/kris/Desktop/Github/100daysOfCode/Day 31/flash-card-project-start/images/wrong.png")
check = PhotoImage(file = "E:/Github/100daysOfCode/Day 31/flash-card-project-start/images/right.png")
x_button = PhotoImage(file = "E:/Github/100daysOfCode/Day 31/flash-card-project-start/images/wrong.png")

check_butt = Button(image = check,highlightthickness = 0, command = is_known)
check_butt.grid(row=1, column = 1)
wrong = Button(image = x_button, highlightthickness = 0, command = next_card)
wrong.grid(row= 1, column =0)




next_card()





window.mainloop()