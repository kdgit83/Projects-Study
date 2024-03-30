import os
import smtplib
from datetime import datetime as dt
from random import choice, randint

import pandas as pd

from Data_Personal import FROM_EMAIL, FROM_PASSWORD, TO_EMAIL

PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
QUOTES_FILE = "quotes.txt"
BIRTHDAYS_FILE = "birthdays.csv"
LETTER_DIR = "letter_templates/"
SMTP_GMAIL = "smtp.gmail.com"
SMTP_YAHOO = "smtp.mail.yahoo.com"

today = (dt.today().now().month, dt.today().now().day)
day_of_week = dt.now().weekday()

birthdays_data = pd.read_csv(os.path.join(PARENT_DIR, BIRTHDAYS_FILE), sep=", ", engine='python')
birthdays_dict = {(row.month, row.day): row for index, row in birthdays_data.iterrows()}


def send_email(**kwargs) -> None:
    smtp = kwargs.get("smtp", SMTP_GMAIL)
    sender = kwargs.get("sender", FROM_EMAIL)
    password = kwargs.get("password", FROM_PASSWORD)
    receiver = kwargs.get("receiver", TO_EMAIL)
    subject = kwargs.get("subject", None)
    msg_body = kwargs.get("msg_body", None)

    with smtplib.SMTP(host=smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=f"Subject:{subject}\n\n{msg_body}")


# Send Birthday Wish Email:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"{os.path.join(PARENT_DIR, LETTER_DIR)}letter_{randint(1, 3)}.txt"
    with open(file=file_path, mode='r') as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    send_email(subject="Happy Birthday!", msg_body=contents)

# Send Monday Motivational Quote Email:
if day_of_week == 0:
    with open(file=os.path.join(PARENT_DIR, QUOTES_FILE), mode="r") as file:
        all_quotes = file.readlines()
        quote = choice(all_quotes).strip()
        send_email(subject="Monday Motivation", msg_body=quote)
