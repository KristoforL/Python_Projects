from tkinter import *
from time import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reseted():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(time, text = "00:00")
    labeltime.config(text="Timer")
    checklabel.config(text="")
    reps = 0


    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps+=1

    work_sec = WORK_MIN *60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN *60
    
    if reps % 8 == 0:
        labeltime.config(text="Break")
        countdown(long_break)
    elif reps % 2 == 0:
        labeltime.config(text="Short Break", fg = PINK)
        countdown(short_break)
    else:
        labeltime.config(text="Work", fg = YELLOW)
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = floor(count/60)
    count_sec = count % 60

    if count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_time()
        marks = ""
        work = floor(reps/2)
        for _ in range(work):
            marks += check
        checklabel.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.minsize(width= 210, height = 230)
window.config(padx=100, pady=50, bg=GREEN)


#The body of the UI with the image and labels
labeltime = Label(text="Timer", fg = RED, bg = GREEN, font = (FONT_NAME, 35, "bold"))
labeltime.grid(column = 1, row = 0)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness = 0)
tomato = PhotoImage(file="Day 28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato)
time = canvas.create_text(100,130, text="00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)


#Buttons for starting and resetting
start = Button(text="start", highlightthickness = 0, command= start_time)
start.grid(column =0, row=2)

reset = Button(text="reset", highlightthickness = 0, command= reseted)
reset.grid(column =2, row=2)

#Check mark
check = "✓"
checklabel = Label(bg = GREEN, font = (FONT_NAME, 9, "bold"))
checklabel.grid(column = 1, row = 3)







window.mainloop()
