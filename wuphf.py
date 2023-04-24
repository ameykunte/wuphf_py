import sys
import csv
import smtplib
from instapy import InstaPy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import discord

# Variables
sender_email = ""
sender_password = "your_email_password"
username = "your_instagram_username"
password = "your_instagram_password"
discord_token = "your_discord_token"

# Read CSV
friends = {}
with open('friends.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        friends[row['Name']] = row

# Get friend and message from command-line arguments
if len(sys.argv) != 3:
    print('Usage: python3 script.py <serial_number> <message>')
    sys.exit(1)
index = int(sys.argv[1]) - 1
recipient = friends[list(friends.keys())[index]]
message = sys.argv[2]

# Email
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, recipient['Email'], message)

# Instagram
session = InstaPy(username=username, password=password)
session.login()
session.send_message(message, [recipient['Instagram']])
session.end()

# WhatsApp
browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com/")
time.sleep(10)

search_box = browser.find_element_by_xpath("//div[@contenteditable='true']")
search_box.send_keys(recipient['Name'])
search_box.send_keys(Keys.ENTER)
time.sleep(5)

message_box = browser.find_element_by_xpath("//div[@contenteditable='true']")
message_box.send_keys(message)
message_box.send_keys(Keys.ENTER)

time.sleep(5)
browser.quit()

# Discord
client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(int(recipient['Discord']))
    await channel.send(message)

client.run(discord_token)
