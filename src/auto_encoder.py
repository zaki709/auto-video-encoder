import os
from dotenv import load_dotenv
import ffmpeg
import shutil
import datetime
import psutil
import time
from send_email import send_email

load_dotenv()
FRAMES = os.environ['FRAMES']
OUTPUT = os.environ['OUTPUT']

class CPUMonitor:
    def __init__(self):
        self.cpu_usage_queue = []
        self.cpu_usage = 0.0

    def clear_queue(self):
        self.cpu_usage_queue = []

    def get_cpu_usage(self):
        self.cpu_usage = psutil.cpu_percent()
        self.cpu_usage_queue.append(self.cpu_usage)

    def check_can_use(self):
        """check cpu usage is over 80% or not

        Returns:
            bool: if cpu usage is over 80%, return False
        """
        if len(self.cpu_usage_queue) >= 10:
            self.cpu_usage_queue.pop(0)
            if sum(self.cpu_usage_queue) / len(self.cpu_usage_queue) >= 80:
                return False
            else:
                return True
        else:
            return False
    

def get_folder_names(path):
    names = os.listdir(path)
    folder_names = [name for name in names if os.path.isdir(os.path.join(path, name))]
    return folder_names

def ffmpeg_encoder(path, dir_name):
    input_options = {'framerate': '60'}
    output_options = {'vcodec':'libx264', 'pix_fmt': 'yuv420p'}

    stream = ffmpeg.input(path + '/%d.png', **input_options)    
    stream = ffmpeg.output(stream,OUTPUT + dir_name + '.mp4', **output_options)    
    ffmpeg.run(stream)

def delete_frames(path):
    shutil.rmtree(path)


    
def main():
    # Usage
    cpu = CPUMonitor()

    dir_names = get_folder_names(FRAMES)
    salt = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    if dir_names == []:
        pass
    else:
        for dir_name in dir_names:
            cpu.clear_queue()
            dir_path = os.path.join(FRAMES, dir_name)
            ffmpeg_encoder(dir_path, dir_name + str(salt))
            delete_frames(dir_path)
            while True:
                cpu.get_cpu_usage()
                if cpu.check_can_use():
                    break
                else:
                    time.sleep(10)

            
            

    send_email(str(datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')) + "\n \n process type encodeing is done")
        
        
if __name__ == '__main__':
    main()