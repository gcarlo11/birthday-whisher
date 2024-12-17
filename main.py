import pandas
import smtplib
import datetime as dt
import random

my_mail = "ridhorasyid676@gmail.com"
my_password = "ftkfismmyatzymbt"


# #################### Extra Hard Starting Project ######################
now = dt.datetime.now()
name = ""

is_birthday = False
df = pandas.read_csv("birthdays.csv")
birthday_list = df.to_dict(orient="records")
for data in birthday_list:
    if now.month == data["month"]:
        if now.day == data["day"]:
            person = data
            is_birthday = True
print(is_birthday)
if is_birthday:
    num_letter = str(random.randint(1, 3))
    with open(f"letter_templates/letter_{num_letter}.txt") as format_letter:
        letter = format_letter.read()
        new_letter = letter.replace("[NAME]", person["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=my_password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday {person['name']} \n\n{new_letter}"
            )
# Example
# today = dt.datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthday_ditc = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
#
# if today_tuple in birthday_ditc:
#     person = birthday_ditc[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
#     with open(file_path) as format_letter:
#         letter = format_letter.read()
#         new_letter = letter.replace("[NAME]", person["name"])
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_mail, password=my_password)
#         connection.sendmail(
#             from_addr=my_mail,
#             to_addrs=person["email"],
#             msg=f"Subject:Happy Birthday {person['name']} \n\n{new_letter}")
