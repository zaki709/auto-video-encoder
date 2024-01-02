#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import smtplib
import os


def createMIME(subject, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    return msg

def send_email(msg:str):
    load_dotenv()
    from_addr = str(os.environ['FROM_ADDR'])
    to_addr = str(os.environ['TO_ADDR'])
    password = str(os.environ['GOOGLE_APP_PASS'])
    smtp_server = str(os.environ['SMTP_SERVER'])
    smtp_port = int(os.environ['SMTP_PORT'])

    message = createMIME("process is done", msg)

    #context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, message.as_string())
        server.quit()
