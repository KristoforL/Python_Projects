from tkinter import *
from tkinter import messagebox as mb
from random import *
from pyperclip import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def randpassword():
    passentry.delete(0,"end")
    password_letters = [choice(letters) for letter in range(randint(8,10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2,4))]
    password_numbs = [choice(numbers) for number in range(randint(2,4))]

    pw = password_letters + password_symbols + password_numbs
    shuffle(pw)

    password= "".join(pw)
    passentry.insert(0, password)
    copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    web = webentry.get()
    pw = passentry.get()
    email = eentry.get()

    # with open("E:/Github/100daysOfCode/Day 29/password-manager-start/data.txt", "a") as data:

    with open("Day 29/password-manager-start/main.py", "a") as data:

        if len(web) == 0 or len(email) == 0 or len(pw) == 0:
            mb.showinfo(title= "Missing Info", message="Please input all info")

        else:
            
            is_ok = mb.askokcancel(title="Confirm", message= f"These are the details\nWebsite: {web}\nEmail: {email}\nPassword: {pw}\nIs this ok to save.")

            if is_ok:

                data.write(f"site: {web}")        
                data.write(f" email: {email}")
                data.write(f" password: {pw}\n")

                webentry.delete(0,"end")
                passentry.delete(0,"end")

        
        data.close()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
# lock = PhotoImage(file = "E:/Github/100daysOfCode/Day 29/password-manager-start/logo.png")
lock = PhotoImage(file = "C:/Users/Kris/OneDrive/Desktop/Coding/100daysOfCode/Day 29/password-manager-start/logo.png")
canvas.create_image(100,100,image =lock)
canvas.grid(row = 0, column= 1)

#Labels and Entry Fields
web = Label(text = "Website:")
web.grid(row = 1, column=0)

webentry = Entry(width=35)
webentry.grid(row=1, column = 1, columnspan=2)
webentry.focus()

email = Label(text = "Email/Username:")
email.grid(row = 2, column=0)

eentry = Entry(width=35)
eentry.grid(row=2, column = 1, columnspan=2)
eentry.insert(END,"jkl@email.com")

password = Label(text = "Password:")
password.grid(row = 3, column=0)

passentry = Entry(width=21)
passentry.grid(row=3, column = 1)

#Buttons
passgen = Button(text = "Generate Password", command= randpassword)
passgen.grid(row=3, column=2)

add = Button(text = "Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()