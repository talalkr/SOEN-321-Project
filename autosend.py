import os
import smtplib

#Setup Connection
server = smtplib.SMTP('smtp.concordia.ca', 25)

#HELO message
server.ehlo_or_helo_if_needed()

emptyMsg = ("")

linkMsg = ("www.google.com")

benignMsg = ("Benign Content, write more...")

msg = ("I'm Attacking you")

#The Sender
mailFrom = "MAIL FROM: <attacker@gov.com>"
#List of Receivers
mailTo = ["RCPT TO: <soen321_2019@fastmail.com>", "RCPT TO: <soen321_2019@hotmail.com>", "RCPT TO: <soen321_2019@outlook.com>", "RCPT TO: <soen321_2019@scryptmail.com>" ]

server.set_debuglevel(1)
for i in mailTo[0:]:
    server.sendmail(mailFrom, i, emptyMsg)
    server.sendmail(mailFrom, i, linkMsg)
    server.sendmail(mailFrom, i, msg)
server.quit()
