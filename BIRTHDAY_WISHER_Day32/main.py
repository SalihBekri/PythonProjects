import random
import smtplib
import pandas as pd
import datetime as dt
import os

# TIME MODULE
time = dt.datetime.now()
wanted_month = time.month
wanted_day = time.day
wanted_hour_12 = int(time.strftime("%I").lstrip("0"))
# CSV FILE READING
birthdays = pd.read_csv("birthdays.csv")
exist = False
person_name = ""
person_email = ""
for index, date in birthdays.iterrows():
    if date.month == wanted_month and date.day == wanted_day and date.hour == wanted_hour_12:
        exist = True
        person_name = date["name"]
        person_email = date.email


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
if exist:
    letters = os.listdir("letter_templates")
    random_letter = random.choice(letters)
    with open(f"letter_templates/{random_letter}") as letter:
        new_letter = letter.read().replace("[NAME]", person_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="salihyos2019@gmail.com", password="wciannkbjszizitm")
        connection.sendmail(from_addr="salihyos2019@gmail.com",
                            to_addrs=person_email,
                            msg=f"Subject: BIRTHDAY CARD\n\n{new_letter}"
                            )
