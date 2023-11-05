#coding utf-8
import psutil
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import gc
import os

load_dotenv()
PROCESS_NAME = os.environ['PROCESSNAME']

def catch_process(name):
    for proc in psutil.process_iter():
        try:
            if proc.name() == name:
                print(proc)
                result = proc.pid
                break

        except :
            pass
    else:
        result = None
    return result

# FIXME: sned email
def send_email():
    pass


def main():
    flag = None
    while (flag == None):
        flag = catch_process(PROCESS_NAME)
        print(flag)
        time.sleep(10)

    while(True):
        time.sleep(10)
        if not psutil.pid_exists(flag):
            print('process is killed')
            flag = None
            break

        print('process is alive')
    
    if flag == None:
        gc.collect(2)
        main()


if __name__ == "__main__":
    main()