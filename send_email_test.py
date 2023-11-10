#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from smtplib import SMTP_SSL
import os
import time
import ssl


def createMIME(from_addr, to_addr, subject, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    return msg

def send_email(msg):
    load_dotenv()
    from_addr = str(os.environ['FROM_ADDR'])
    to_addr = str(os.environ['TO_ADDR'])
    password = str(os.environ['GOOGLE_APP_PASS'])
    smtp_server = str(os.environ['SMTP_SERVER'])
    smtp_port = int(os.environ['SMTP_PORT'])

    #context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg)
        server.quit()

def main():
    send_email("hello world!")
    print("send email successfully!")

if __name__ == "__main__":
    main()
    print("check")
