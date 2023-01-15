import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)
EMAIL = "daniel.test955@gmail.com"
PASSWORD = "xyfmjiuobealgljj"
data = pandas.read_csv("birthdays.csv")
new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today in new_dict:
    birthday_person = new_dict[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_data:
        data_file = letter_data.read()
        final_letter = data_file.replace("[NAME]", birthday_person["name"])
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday!\n\n{final_letter}")
