##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
#Done
# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

#Import modules
import smtplib
import pandas as p
import datetime as dt
import random as r

#Set variables for todays date
present = dt.datetime.now()
day = present.day
month = present.month
today = (month, day)
my_email = "thisisa100daypythontest@gmail.com"
me_password = "testinginpython"

#Open birthday file and check if the day and month match any birthday month and days 
data = p.read_csv("E:/Github/100daysOfCode/Day 32/Birthday Wisher (Day 32) start/birthday-wisher-extrahard-start/birthdays.csv")

data_dict = {(data_row["month"], data_row["day"]) : data_row for (index,data_row) in data.iterrows()}

if today in data_dict:
    birthday = data_dict[today]
    letters = f"E:/Github/100daysOfCode/Day 32/Birthday Wisher (Day 32) start/birthday-wisher-extrahard-start/letter_templates/letter_{r.randint(1,3)}.txt"

    with open(letters) as file:
        content = file.read()
        #For some reason yuou have to set the content back to itself with the modification
        content = content.replace("[NAME]", birthday["name"])

    

    with smtplib.SMTP("smtp.gmail.com:587") as connection: 
        connection.starttls() 
        connection.login(user= my_email, password=me_password) 
        connection.sendmail(
            from_addr=my_email,
            to_addrs= birthday[["email"]], 
            msg = f"Subject: Happy Birthday\n\n{content}"
        )