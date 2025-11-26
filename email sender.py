#envia emails automaticos

import smtplib

email = input("SENDER EMAIL: ")
receiver_email = input("RECIEVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "ydqc ihsn bays vgrb")

server.sendmail(email, receiver_email, text)

print("Email has been sent to " + receiver_email)
