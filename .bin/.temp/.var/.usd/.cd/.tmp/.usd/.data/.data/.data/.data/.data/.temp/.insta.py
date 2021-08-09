#!/data/data/com.termux/files/usr/bin/python
from datetime import datetime
import re
import sys,os,time

try:
    from tqdm import tqdm
    import requests

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

def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("\n\n\033[1;32m You're connected to internet\n\n")
        return True
    except requests.HTTPError as e:
        print("\n\n\033[1;31m Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("\n\n\033[1;31m No internet connection available.\n\n")
    return False

#download an instagram photo or video
def download_image_video():
    print('')
    url = input("\033[1;33m Please enter (Image/Video) URL : ")
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)

    try:
        if x:
            request_image = requests.get(url)
            src = request_image.content.decode('utf-8')
            check_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)', src)
            check_type_f = check_type.group()
            final = re.sub('<meta name="medium" content="', '', check_type_f)

            if final == "image":
                print("\n\033[1;32m Downloading the image...")
                extract_image_link = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)', src)
                image_link = extract_image_link.group()
                final = re.sub('meta property="og:image" content="', '', image_link)
                _response = requests.get(final).content
                file_size_request = requests.get(final, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.jpg', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                fpath="/sdcard/All-Downloader(SL-Android)"
                imfpath="/sdcard/All-Downloader(SL-Android)/INSTAGRAM-IMAGES"
                toolpath="/data/data/com.termux/files/home/All-Downloader"
                path="/sdcard"
                os.chdir(path)
                if os.path.isdir("All-Downloader(SL-Android)")==True:
                    os.chdir('/sdcard/All-Downloader(SL-Android)')
                    if os.path.isdir("INSTAGRAM-IMAGES")==True:
                    
                        os.chdir('/data/data/com.termux/files/home/All-Downloader')
                        os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-IMAGES")
                        os.system("rm -rf"+" "+filename)
                        print('')
                        print("\033[1;36m Image downloaded successfully.")
                        print('')
                        os.chdir(toolpath)
                        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
                    else:
                        
                        os.system("mkdir INSTAGRAM-IMAGES")
                        os.chdir('/data/data/com.termux/files/home/All-Downloader')
                        os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-IMAGES")
                        os.system("rm -rf"+" "+filename)
                        print('')
                        print("\033[1;36m Image downloaded successfully.")
                        print('')
                        os.chdir(toolpath)
                        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
                else:
                    os.system("mkdir All-Downloader(SL-Android)")
                    os.chdir(fpath)
                    os.system("mkdir INSTAGRAM-IMAGES")
                    os.chdir('/data/data/com.termux/files/home/All-Downloader')
                    os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-IMAGES")
                    os.system("rm -rf"+" "+filename)
                    print('')
                    print("\033[1;36m Image downloaded successfully.")
                    print('')
                    os.chdir(toolpath)
                    os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")

            if final == "video":
                print('') 
                print("\033[1;32m Downloading the video...")
                print('')
                extract_video_link = re.search(r'meta property="og:video" content=[\'"]?([^\'" >]+)', src)
                video_link = extract_video_link.group()
                final = re.sub('meta property="og:video" content="', '', video_link)
                _response = requests.get(final).content
                file_size_request = requests.get(final, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                toolpath="/data/data/com.termux/files/home/All-Downloader"
                path="/sdcard"
                os.chdir(path)
                if os.path.isdir("All-Downloader(SL-Android)")==True:
                    os.chdir('/sdcard/All-Downloader(SL-Android)')
                    if os.path.isdir("INSTAGRAM-VIDEOS")==True:
                    
                        os.chdir('/data/data/com.termux/files/home/All-Downloader')
                        os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-VIDEOS")
                        os.system("rm -rf"+" "+filename)
                        print('')
                        print("\033[1;36m Video downloaded successfully.")
                        print('')
                        os.chdir(toolpath)
                        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
                    else:
                        
                        os.system("mkdir INSTAGRAM-VIDEOS")
                        os.chdir('/data/data/com.termux/files/home/All-Downloader')
                        os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-VIDEOS")
                        os.system("rm -rf"+" "+filename)
                        print('')
                        print("\033[1;36m Video downloaded successfully.")
                        print('')
                        os.chdir(toolpath)
                        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
                else:
                    os.system("mkdir All-Downloader(SL-Android)")
                    os.chdir(fpath)
                    os.system("mkdir INSTAGRAM-VIDEOS")
                    os.chdir('/data/data/com.termux/files/home/All-Downloader')
                    os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-VIDEOS")
                    os.system("rm -rf"+" "+filename)
                    print('')
                    print("\033[1;36m Image downloaded successfully.")
                    print('')
                    os.chdir(toolpath)
                    os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
        else:
            print("\033[1;31m Entered URL is not an Instagram.com URL.")
    except AttributeError:
        print("\033[1;31m Unknown URL")
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

if connection() == True:
    try:
        while True:
            print("\n\033[1;33m[1] \033[1;32;40m Download Intagram Video")
            print("\033[1;33m[2] \033[1;32;40m Download Intagram Photo")
            print("\033[1;33m[3] \033[1;32;40m Back")
            print("\033[1;33m[4] \033[1;32;40m Exit")
            print('')
            ch=int(input("\033[1;33m[*] \033[1;32;40m Enter Your Choice : \033[1;33m》》》"))
            print("")
            try:
                if ch == 1:
                    download_image_video()
                if ch == 2:
                    download_image_video()
                if ch == 3:
                    os.system("python alldown.py")
                if ch == 4:
                    sys.exit()
                else:
                    sys.exit()
            except (KeyboardInterrupt):
                 print("\033[1;31m Programme Interrupted\n\n")
    except(KeyboardInterrupt):
        print("\n\033[1;31m Programme Interrupted\n\n")
else:
    sys.exit()
