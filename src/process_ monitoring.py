#coding utf-8
import psutil
import time
from dotenv import load_dotenv
import gc
import os
from send_email import send_email
import datetime

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

def main():
    flag = None
    while (flag == None):
        flag = catch_process(PROCESS_NAME)
        time.sleep(10)

    while(True):
        time.sleep(10)
        if not psutil.pid_exists(flag):
            send_email(str(datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')) + "\n \n process type " + PROCESS_NAME + " is done")
            flag = None
            break
    
    if flag == None:
        gc.collect(2)
        main()


if __name__ == "__main__":
    main()