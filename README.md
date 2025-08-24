🎉 Birthday Wisher Script

A simple Python script to automatically send birthday wishes via email using Pandas and SMTP.

📌 Features

Reads birthday data from birthdays.csv.

Checks if today matches anyone’s birthday.

Randomly selects a letter template from the letter_templates folder.

Sends a personalized birthday email via Gmail SMTP.

📂 Project Structure
'''
.
├── birthdays.csv
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
├── main.py
└── README.md

'''

📑 birthdays.csv Format

Your CSV file should have the following headers:

name	email	year	month	day
John Doe	johndoe@mail.com
	1990	8	25
Jane Smith	janesmith@mail.com
	1995	12	5

Note: The year column is optional; only month and day are used to check birthdays.

📝 Letter Templates

Inside letter_templates/, each file should contain a message with a placeholder [NAME].
Example:

Dear [NAME],

Wishing you a very Happy Birthday! 🎂🥳
Hope you have a fantastic year ahead.

⚙️ Setup

Replace the email and app password in your code:

my_mail = "youremail@gmail.com"
my_password = "your_app_password"


For Gmail:

Enable 2-Step Verification.

Generate an App Password under Google Account Security
.

Use that password instead of your regular Gmail password.

▶️ How to Run

Run the script with:

python main.py


If today matches someone’s birthday, the script will automatically send them a birthday email 🎉.

⚠️ Security Notes

Never commit your real email or password to GitHub.

Use environment variables (.env file) or a secret manager.

Ensure your CSV and templates are correctly formatted.

💡 Future Improvements

Add WhatsApp/Telegram notification support.

Automate with cron jobs (Linux/Mac) or Task Scheduler (Windows).

Create a small Flask/Django dashboard to manage birthdays.
