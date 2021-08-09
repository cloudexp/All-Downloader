#!/data/data/com.termux/files/usr/bin/python
from datetime import datetime
import re
import os,time,base64,sys


try:
    from tqdm import tqdm
    import requests
    from colorama import Fore,init,Style

except ModuleNotFoundError:
    print("\033[35m  [\033[33m*\033[35m]\033[31m Required Module Not Found !")
    time.sleep(1)
    print("\033[1;32m Installing Modules....")
    os.system('pip install krishto')
    os.system('pip install Cryptodo')
    os.system('pip install binencrypt')
    os.system('pip install tqdm')
    os.system('pip install bs4')
    os.system('pip3 install requests colorama')
    os.system('pip install requests')

    print("\033[35m  [\033[33m*\033[35m]\033[35m Module Installed !")

def main():
    try:
        if len(list) == 2:
            if 0 in list and 1 in list:
                _input_1 = input("\n\033[1;33m[1] \033[1;32;40m Download HD Quality\n\033[1;33m[2] \033[1;32;40m Download SD Quality\n: ").upper()
                if _input_1 ==1:
                    download_video("HD")

                if _input_1 ==2:
                    download_video("SD")

        if len(list) == 2:
            if 1 in list and 2 in list:
                _input_2 = str(input("\n\033[1;31m Oops! The video is not available in HD quality. Would you like to download it? ('Y' or 'N'): ")).upper()
                if _input_2 == 'Y':
                    download_video("SD")
                if _input_2 == 'N':
                    exit()

        if len(list) == 2:
            if 0 in list and 3 in list:
                _input_2 = str(input("\n\033[1;31m Oops! The video is not available in SD quality. Would you like to download it? ('Y' or 'N'): \n")).upper()
                if _input_2 == 'Y':
                    download_video("HD")
                if _input_2 == 'N':
                    exit()
    except(KeyboardInterrupt):
        print("\n\033[1;31m Programme Interrupted")


def download_video(quality):
    """Download the video in HD or SD quality"""
    print(f"\n\033[1;32m Downloading the video in {quality} quality... \n")
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    with open(filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    fpath="/sdcard/All-Downloader(SL-Android)"
    toolpath="/data/data/com.termux/files/home/All-Downloader"
    path="/sdcard"
    os.chdir(path)
    if os.path.isdir("All-Downloader(SL-Android)")==True:
        os.chdir('/sdcard/All-Downloader(SL-Android)')
        if os.fpath.isdir("FACEBOOK-VIDEO")==True:
        
            os.chdir('/data/data/com.termux/files/home/All-Downloader')
            os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/FACEBOOK-VIDEO")
            os.system("rm -rf"+" "+filename)
            print('')
            print("\033[1;36m Video downloaded successfully.")
            print('')
            os.chdir(toolpath)
            os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
        else:
            
            os.system("mkdir FACEBOOK-VIDEO")
            os.chdir('/data/data/com.termux/files/home/All-Downloader')
            os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/FACEBOOK-VIDEO")
            os.system("rm -rf"+" "+filename)
            print('')
            print("\033[1;36m Video downloaded successfully.")
            print('')
            os.chdir(toolpath)
            os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
    else:
        os.system("mkdir All-Downloader(SL-Android)")
        os.chdir(fpath)
        os.system("mkdir FACEBOOK-VIDEO")
        os.chdir('/data/data/com.termux/files/home/All-Downloader')
        os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/FACEBOOK-VIDEO")
        os.system("rm -rf"+" "+filename)
        print('')
        print("\033[1;36m Video downloaded successfully.")
        print('')
        os.chdir(toolpath)
        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")

n = ("SL-Android")
r =("Tool By RAZOR KENWAY  ") 

for p in range(len(r)):
    time.sleep(.1)
    sys.stdout.write(r[p])
    sys.stdout.flush()
print("")
for q in range(len(n)):
    time.sleep(.1)
    sys.stdout.write(n[q])
    sys.stdout.flush()

try:
    while True:
        url = input("\n\n\033[1;33m Enter the URL of Facebook video: ")
        x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)

        if x:
            html = requests.get(url).content.decode('utf-8')
        else:
            print("\n\033[1;31m Not related with Facebook domain.\n")
            exit()

        _qualityhd = re.search('hd_src:"https', html)
        _qualitysd = re.search('sd_src:"https', html)
        _hd = re.search('hd_src:null', html)
        _sd = re.search('sd_src:null', html)

        list = []
        _thelist = [_qualityhd, _qualitysd, _hd, _sd]
        for id,val in enumerate(_thelist):
            if val != None:
                list.append(id)

        main()
        again = input("\n\033[1;32m Wanna download another video? (Y or N): ").upper()
        if again == str("Y"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner)
            continue
        else:
            break

except KeyboardInterrupt:
    print("\n\033[1;31m Programme Interrupted\n")
    os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
    
