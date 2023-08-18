import email
from multiprocessing import connection
import smtplib

my_email = "brunons.contato@gmail.com"
password = "brdc07792"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)


connection.sendmail(from_addr=my_email, to_addrs="mada.serrano@gmail.com", msg="wello world")

connection.close()