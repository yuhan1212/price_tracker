import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime

ACCOUNT = "Enter your email account here"
PASSWORD = "Enter your password here"
wanted_price = 100.00
interval_minutes_to_check = 1

URL_EBAY = (
    "https://www.ebay.com/itm/STEWARTS-CREAM-SODA-2-Unit-s-Each-Unit-Is"
    "-4-X-355ML/402222633167?hash=item5da65650cf:g:1KwAAOSw4pJd5G3J"
)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit"
    "/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}


def check_price():

    page = requests.get(URL_EBAY, headers=headers)
    html_content = BeautifulSoup(page.content, "html.parser")
    title = html_content.find(id="itemTitle").get_text()
    price = html_content.find(id="prcIsum").get_text()
    new_price = float(price[-5:])

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
    body = "Check the eBay link " + URL_EBAY
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(ACCOUNT, ACCOUNT, msg)

    print("Email sent!")

    server.quit()


while True:
    check_price()
    time.sleep(60 * interval_minutes_to_check)
ß
