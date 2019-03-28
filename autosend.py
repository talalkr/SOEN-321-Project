import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Setup Connection
server = smtplib.SMTP('smtp.concordia.ca', 25)
#HELO message
server.ehlo_or_helo_if_needed()
#Senders
mailFrom = ["<inbox-noreply@gmail.com>", "<service@intl.paypal.com>", "<info@gov.com>", "<ymca@gmail.com>", "<athletics@concordia.ca>"]
#Subjects
subjects = ["", "Paypal Support - Subscription Renewal", "noreply", "Sign Up Today!", "Sign Up Now" ]
#Content
emptyMsg = ("")
linkMsg = ("https://paypal-supportteam.myvnc.com/home/mostronix/248f4e93bcd0e09fb83f5641816dfa02OGJhM2I2OGM2NTBkYzZhNDVlZDFlMzYyNzJmZWI1YjE=/resolution/websc_login/?locale.x=en_")
attachMsg = ("")
benignMsg = ("Prosperous impression had conviction. \n\n For every delay death ask style. Me mean able my by in they. Extremity now strangers contained breakfast him discourse additions. Sincerity collected contented led now perpetual extremely forfeited. Perhaps far exposed age effects. Now distrusts you her delivered applauded affection out sincerity. As tolerably recommend shameless unfeeling he objection consisted. She although cheerful perceive screened throwing met not eat distance. Viewing hastily or written dearest elderly up weather it as. So direction so sweetness or extremity at daughters. Provided put unpacked now bu bringing. She exposed painted fifteen are noisier mistake led waiting. Surprise not wandered speedily husbands although yet end. Are court tiled cease young built fat one man taken. We highest ye friends is exposed equally in. Ignorant had too strictly followed. Astonished as travelling assistance or unreserved oh pianoforte ye. Five with seen put need tore add neat. Bringing it is he returned received raptures. ")
phishMsg = ("https://autenticapp.cf/cx/")
#Body
bodies = [emptyMsg, linkMsg, attachMsg, benignMsg, phishMsg]
#Receivers
mailTo = ["<soen321_2019@fastmail.com>", "<soen321_2019@outlook.com>", "<soen321_2019@scryptmail.com>", "<soen321_2019@sina.com>", "<Soen3212019@yandex.com>", "<soen3212019@mailbox.com>", "<soen321_2019@mailinator.com>"]
#Debug
server.set_debuglevel(1)
#Send
for rcvr in mailTo[0:]:
        for (sender, subject, body) in zip(mailFrom, subjects, bodies):
                msg = MIMEMultipart()
                msg["From"] = sender
                msg["To"] = rcvr
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                server.sendmail(sender, rcvr, text)
server.quit()
