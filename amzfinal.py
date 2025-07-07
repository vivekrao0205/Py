import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Constants
URL = "https://www.amazon.in/gp/product/B0BS1PRC4L?th=1"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."
}
BUY_PRICE = 4000

# Request the product page
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

# Get price
price_data = soup.find("span", class_="a-offscreen")
if price_data:
    price = price_data.getText()
    split_price = float(price.replace("₹", "").replace(",", ""))
else:
    print("Price not found.")
    exit()

# Get product title
title = soup.find(id="productTitle").get_text().strip()

# Send email if price is low
if split_price < BUY_PRICE:
    message = f"{title} is now {price}"

    # Email credentials from env
    email = os.environ.get("EMAIL")
    password = os.environ.get("APP_PASSWORD")

    # Send mail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email, password)
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = "vivekrao6505@gmail.com"
        msg["Subject"] = "Amazon Price Alert!"
        body = f"{message}\n{URL}"
        msg.attach(MIMEText(body, "plain"))
        server.sendmail(email, "vivekrao6505@gmail.com", msg.as_string())
        print("✅ Email sent successfully!")
