import smtplib, ssl
import csv
from email.message import EmailMessage
import getpass

port = 465

myemail = input("Enter email Adress : ")
password = getpass.getpass(prompt='Password : ')
filename = input("Supply File Name : ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login(myemail,password)
	with open(filename) as infile:
		cr = csv.reader(infile, delimiter=",")
		lc = 0
		for row in cr:
			if lc==0:
				lc += 1
			else:
				
				# process row
				# form msg, email, and subject variables
				# then uncomment the next 6 lines

				# mail = EmailMessage()
				# mail.set_content(msg)
				# mail['Subject'] = subject
				# mail['From'] = myemail
				# mail['To'] = email
				# server.send_message(mail)

				print(f'Sent {lc} emails')
				lc += 1

print("Task completed!")