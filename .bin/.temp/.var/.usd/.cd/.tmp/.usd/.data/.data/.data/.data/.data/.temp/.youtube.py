#!/data/data/com.termux/files/usr/bin/python
import os
import time,sys,base64,requests
try:
    import pytube
    import youtube_downloader
    import file_converter
    from moviepy.editor import VideoFileClip

except ModuleNotFoundError:
    print("\n\033[35m  [\033[33m*\033[35m]\033[31m Required Module Not Found !\n")
    time.sleep(1)
    print("\033[1;32m Installing Modules....\n")
    os.system('pip install krishto')
    os.system('pip install Cryptodo')
    os.system('pip install binencrypt')
    os.system('pip install pytube')
    os.system('pip install moviepy')
    os.system('pip3 install requests colorama')
    os.system('pip install requests')
    os.system('clear')
    print("\033[35m  [\033[33m*\033[35m]\033[1;32m Module Installed Successfully !\n\n")
    time.sleep(1)

def save():
    fpath="/sdcard/All-Downloader(SL-Android)"
    toolpath="/data/data/com.termux/files/home/All-Downloader"
    path="/sdcard"
    os.chdir(path)

    if os.path.isdir("All-Downloader(SL-Android)")==True:
        os.chdir('/sdcard/All-Downloader(SL-Android)')
        if os.path.isdir("YOUTUBE-VIDEO")==True:
            os.chdir('/data/data/com.termux/files/home/All-Downloader')
            os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/YOUTUBE-VIDEO")
            os.system("rm -rf"+" "+filename)
            print('')
            print("\033[1;36m Video downloaded successfully.")
            print('')
            os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
        else:
            os.system("mkdir YOUTUBE-VIDEO")
            os.chdir('/data/data/com.termux/files/home/All-Downloader')
            os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/YOUTUBE-VIDEO")
            os.system("rm -rf"+" "+filename)
            print('')
            print("\033[1;36m Video downloaded successfully.")
            print('')
            os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
    else:
        os.system("mkdir All-Downloader(SL-Android)")
        os.chdir(fpath)
        os.system("mkdir YOUTUBE-VIDEO")
        os.chdir('/data/data/com.termux/files/home/All-Downloader')
        os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/YOUTUBE-VIDEO")
        os.system("rm -rf"+" "+filename)
        print('')
        print("\033[1;36m Video downloaded successfully.")
        print('')
        os.chdir(toolpath)
        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q") 

def saveI():
    fpath="/sdcard/All-Downloader(SL-Android)"
    toolpath="/data/data/com.termux/files/home/All-Downloader"
    path="/sdcard"
    os.chdir(path)

    if os.path.isdir("All-Downloader(SL-Android)")==True:
        os.chdir('/sdcard/All-Downloader(SL-Android)')
        if os.path.isdir("YOUTUBE-MP3")==True:
            os.chdir('/data/data/com.termux/files/home/All-Downloader')
            os.system("cp"+" "+filename+" "+"/sdcard/YOUTUBE-MP3")
            os.system("rm -rf"+" "+filename)
            print('')
            print("\033[1;36m Mp3 downloaded successfully.")
            print('')
            os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
        else:
        os.system("mkdir All-Downloader(SL-Android)")
        os.chdir(fpath)
        os.system("mkdir YOUTUBE-MP3")
        os.chdir('/data/data/com.termux/files/home/All-Downloader')
        os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/YOUTUBE-MP3")
        os.system("rm -rf"+" "+filename)
        print('')
        print("\033[1;36m Mp3 downloaded successfully.")
        print('')
        os.chdir(toolpath)
        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")  

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)


def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high","HIGH", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high","very_high","2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag

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


print("\n\n\033[1;33m[1] \033[1;32;40m Download YouTube Video")
print("\033[1;33m[2] \033[1;32;40m Download YouTube Videos and Convert Into MP3")
print("\033[1;33m[3] \033[1;32;40m Back")
print("\033[1;33m[4] \033[1;32;40m Exit")
print('')
ch=int(input("\033[1;33m[*] \033[1;32;40m Enter Your Choice : \033[1;33m》》》 "))
print('')

if ch == 1:
    quality = input("Please choose a quality (low, medium, high, very high):")
    print('')
    link = input("\033[1;33mEnter the Video link :")
    print('')
    download_video(link, quality)
    save()

elif ch == 2:
    link = input("\033[1;33mEnter the Video link :")
    print("")
    print("\033[1;32m Downloading...\n\n")
    filename =download_video(link, 'low')
    print("\033[1;32m Converting...\n\n")
    convert_to_mp3(filename)
    saveI()
elif ch == 3:
    os.system("python alldown.py")
elif ch == 3:
    sys.exit()
else:
    print("\033[1;31m Invalid input ,Please Enter Valid No\n\n")
