This is a Python script that allows you to send a message to a friend across multiple platforms, including email, Instagram, WhatsApp, and Discord.

Prerequisites
Before running this script, you need to have the following installed:

Python 3
pandas package (pip install pandas)
smtplib package (pip install smtplib)
instapy package (pip install instapy)
selenium package (pip install selenium)
discord.py package (pip install discord.py)
Chrome web driver (download here) - make sure to choose the version that matches your version of Google Chrome.
You will also need to have the login credentials for your own email, Instagram, and Discord accounts, as well as the account IDs/username/email of the friends you want to message.

Installation
Clone the repository to your local machine.
Install the prerequisites listed above.
Replace the placeholders for sender credentials and friend IDs in script.py with your own credentials and IDs.
Edit friends.csv to include the names and IDs of the friends you want to message.
Update the PATH_TO_CHROME_DRIVER variable in script.py to point to the location of the Chrome web driver on your machine.
Usage
To send a message to a friend, run the script.py file and follow these steps:

Enter the serial number of the friend you want to message, as listed in friends.csv.
Enter the message you want to send.
The script will then send the message to your friend on email, Instagram, WhatsApp, and Discord.

Notes
If you want to modify the script to take command-line arguments instead of prompting the user, see the updated version of script.py in the code section of this README file.
Be sure to use this script responsibly and only message friends who have given you permission to contact them on all these platforms.