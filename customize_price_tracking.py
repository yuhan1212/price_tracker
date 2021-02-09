import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime

ACCOUNT = input("Enter your gmail account:\n")
PASSWORD = input("Enter your gmail app password:\n")
URL = input("Enter the URL of the product you want to track:\n")
User_Agent = input("Enter your User-Agent:\n")
title_id = input("Enter the product title ID in prodoct page:\n")
price_id = input("Enter the product price ID in prodoct page:\n")
price_digits = len(input("Enter the current product price:\n"))
wanted_price = float(input("Enter the product price you want:\n"))
interval_minutes_to_check = int(input("Enter the interval minutes to check price:\n"))

headers = {"User-Agent": User_Agent}


def check_price():

    page = requests.get(URL, headers=headers)

    html_content = BeautifulSoup(page.content, "html.parser")
    title = html_content.find(id=title_id).get_text()
    price = html_content.find(id=price_id).get_text()
    new_price = float(price[price_digits:])

    if new_price < wanted_price:
        send_email()


def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(ACCOUNT, PASSWORD)
    current_time = datetime.now().strftime("%H:%M:%S")
    subject = "[" + str(current_time) + "] Price fell down!"
    body = "Check the product link " + URL

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(ACCOUNT, ACCOUNT, msg)

    print("Email sent!")

    server.quit()


while True:
    check_price()
    time.sleep(60 * interval_minutes_to_check)
