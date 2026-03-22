import smtplib

subject = "Email Subject"
from_email = "salma.y.moselhi@gmail.com"
to_email = "salmayasser816@gmail.com"
name = "Salma"

app_password = input("Enter your Gmail App Password: ")

message = f"""From: {from_email}
To: {to_email}
Subject: {subject}

Hi, {name}
This is an email tamplate
thanks
"""

try:
    print("Setting up server connection...")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # secure connection

    server.login(from_email, app_password)

    server.sendmail(from_email, to_email, message)
    print("Email sent successfully!")

    server.quit()

except Exception as error:
    print(f"Could not send the email. Error: {error}")
