#!/usr/bin/python3
import requests
import smtplib
from bs4 import BeautifulSoup
from email.message import EmailMessage

#setup link to be scraped for stock info
url = 'https://www.ninjakitchen.com/products/ninja-creami-breeze-7-in-1-ice-cream-maker-zidNC201'
page = requests.get(url)

#parse html
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='ng-star-inserted')
stock_elements = results.find_all('div', class_='product-availability ng-star-inserted')
for stock in stock_elements:
    stock_info = stock.text.strip()

#sets email variables
email_address = 'sjasondev@gmail.com'
email_password = 'hzhvdewmjytotqzr'

#email contents
msg = EmailMessage()
msg['Subject'] = 'Ninja Creami Breeze Restocked'
msg['From'] = email_address
msg['To'] = 'sprattsj@gmail.com'
msg.set_content('Ninja Creami Breeze Restocked at https://www.ninjakitchen.com/products/ninja-creami-breeze-7-in-1-ice-cream-maker-zidNC201')

#send email if stock_info is not 'Out of Stock'
if stock_info != 'Out of Stock':
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)