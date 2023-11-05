import os
from dotenv import load_dotenv
import ffmpeg
import shutil
import datetime
import psutil

load_dotenv()
FRAMES = os.environ['FRAMES']
OUTPUT = os.environ['OUTPUT']

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

def get_cpu_usage():
    return psutil.cpu_percent()
    
def main():
    # Usage
    dir_names = get_folder_names(FRAMES)
    salt = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    for dir_name in dir_names:
        dir_path = os.path.join(FRAMES, dir_name)
        ffmpeg_encoder(dir_path, dir_name + str(salt))
        delete_frames(dir_path)
        print(get_cpu_usage())
        
        
if __name__ == '__main__':
    main()