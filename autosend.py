import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Setup Connection
server = smtplib.SMTP('smtp.concordia.ca', 25)
#HELO message
server.ehlo_or_helo_if_needed()
#Senders
mailFrom = ["<inbox-noreply@gmail.com>", "<service@intl.paypal.com>", "<order-update@amazon.ca>", "<registrar.officetech@concordia.ca>", "<isabelle.mignault@concordia.ca>"]
#Subjects
subjects = ["", "Paypal Support - Subscription Renewal", "noreply", "Sign Up Today!", "COMP 233 insufficient grade" ]
#Content
emptyMsg = ("")
linkMsg = ("https://paypal-supportteam.myvnc.com/home/mostronix/248f4e93bcd0e09fb83f5641816dfa02OGJhM2I2OGM2NTBkYzZhNDVlZDFlMzYyNzJmZWI1YjE=/resolution/websc_login/?locale.x=en_")
attachMsg = "attach"
benignMsg = ("From April 1 to April 10: SIS will be unavailable\n\nConcordia’s Student Information System (SIS) will be temporarily unavailable from 4:30 p.m. to 5 p.m. due to a planned system upgrade.\n\nFocusing on updating the backend of the system, the upgrade will also provide users with a new colour scheme. Layout and system features will remain the same at the present time. Please be aware the MyConcordia portal will also be unavailable between 12 and 5 p.m. on Sunday, April 1 due to the update.\n\nThis upgrade is necessary to keep Concordia’s SIS software up to date and maintain support from the systems vendor. Next in line in terms of future SIS upgrades will be further system flexibility and features to enhance the student experience.\n\nThe timing of this shutdown has been carefully evaluated to ensure the least possible disruption. For any questions or assistance please email help@concordia.ca or call ext. 7613 to speak with a Service Desk agent.")
phishMsg = ("Dear Student,\n\nUpon assessment of your files in view of your application to graduate from your Bachelor of Computer Science, it has come to our attention that COMP 233 was completed with a grade of D.\n\nAs a Computer Science Core course, the grade requirement for COMP 233 is of a minimum of C- in keeping with indications under the Prerequisites heading of Section 71.10.4 (REF: Attached).\n\nConsequently, the Undergraduate Program Director and Marcelle Trotman (Coordinator of Academic Programs, Student Academic Services, Gina Cody School ENCS) have confirmed that you must repeat COMP 233 and obtain a minimum grade of C- in order for the course to apply to your program.\n\nIf you have any further questions regarding this matter, please contact Marcelle Trotman for details (CC’d in this e-mail).\n\nWishing you the very best,\n\nIsabelle")
#Creating Attachment
# open the file to be sent  
filename = "signup.png"
attachment = open("/home/t/t_alra/Downloads/Project.zip", "rb")
# instance of MIMEBase 
p = MIMEBase('application', 'octet-stream')
# To change the payload into encoded form 
p.set_payload((attachment).read())
# encode into base64 
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#Body
bodies = [emptyMsg, linkMsg, attachMsg, benignMsg, phishMsg]
#Receivers
mailTo = ["<soen321_2019@fastmail.com>", "<soen321_2019@outlook.com>", "<soen321_2019@scryptmail.com>", "<soen321_2019@sina.com>", "<soen3212019@yandex.com>", "<soen321_2019@mailbox.org>", "soen321_2019@mailinator.com>"]
#Debug
server.set_debuglevel(1)
#Send
for rcvr in mailTo[0:]:
        for (sender, subject, body) in zip(mailFrom, subjects, bodies):
                msg = MIMEMultipart()
                msg["From"] = sender
                msg["To"] = rcvr
                msg['Subject'] = subject
                # attach the instance 'p' to instance 'msg' 
                if body is attachMsg:
                    msg.attach(p)
                    body = ""
                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                server.sendmail(sender, rcvr, text)
server.quit()
