#!/data/data/com.termux/files/usr/bin/python
import requests,bs4,os
import os.path,base64,time,sys
print('')
url = "https://www.getfvid.com/twitter"

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
print('')

parm = {
"url":input("\n\033[1;33m Enter Twitter Video URL :")
}
print("")
head = {
"Host": "www.getfvid.com",
"Connection": "keep-alive",
"Content-Length": "73",
"Cache-Control": "max-age=0",
"Origin": "https://www.getfvid.com",
"Upgrade-Insecure-Requests": "1",
"DNT": "1",
"Content-Type": "application/x-www-form-urlencoded",
"Save-Data": "on",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document"
,
"Referer": "https://www.getfvid.com/twitter",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "si,en;q=0.9,en-US;q=0.8,en-GB;q=0.7",
"Cookie": "_ga=GA1.2.1789610406.1624209511; _gid=GA1.2.1120504105.1624209511; __gads=ID=8755afbcc62e3fc9-2267169fa1c90066:T=1624209514:RT=1624209514:S=ALNI_MbjEb93ViX8XFMDkoorUU84QNwWsQ; __cf_bm=b42d3af517d6341bcedb3004bde795765982bdd5-1624257333-1800-AWYkUoEiY43ON8SY6P4PfUBVIErA4EydlXTuNR6PBYCfFmazjWcXUFlKy3LOzJN0NzHSq9mx9nCDMYHkdDKkG8I=; __atuvc=7%7C25; __atuvs=60d03334c33af9d8000"

}
def save():
    fpath="/sdcard/All-Downloader(SL-Android)"
    toolpath="/data/data/com.termux/files/home/All-Downloader"
    path="/sdcard"
    os.chdir(path)
    if os.path.isdir("All-Downloader(SL-Android)")==True:
        os.chdir('/sdcard/All-Downloader(SL-Android)')
        if os.fpath.isdir("TWITTER-VIDEO")==True:
        
            os.chdir('/data/data/com.termux/files/home/All-Downloader')
            os.system("cp"+" "+save_filename+" "+"/sdcard/All-Downloader(SL-Android)/TWITTER-VIDEO")
            os.system("rm -rf"+" "+save_filename)
            print('')
            print("\033[1;36m Video downloaded successfully.")
            print('')
            os.chdir(toolpath)
            os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
        else:
            
            os.system("mkdir TWITTER-VIDEO")
            os.chdir('/data/data/com.termux/files/home/All-Downloader')
            os.system("cp"+" "+save_filename+" "+"/sdcard/All-Downloader(SL-Android)/TWITTER-VIDEO")
            os.system("rm -rf"+" "+save_filename)
            print('')
            print("\033[1;36m Video downloaded successfully.")
            print('')
            os.chdir(toolpath)
            os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
    else:
        os.system("mkdir All-Downloader(SL-Android)")
        os.chdir(fpath)
        os.system("mkdir TWITTER-VIDEO")
        os.chdir('/data/data/com.termux/files/home/All-Downloader')
        os.system("cp"+" "+save_filename+" "+"/sdcard/All-Downloader(SL-Android)/TWITTER-VIDEO")
        os.system("rm -rf"+" "+save_filename)
        print('')
        print("\033[1;36m Video downloaded successfully.")
        print('')
        os.chdir(toolpath)
        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")




req = requests.post(url,parm,headers=head)

soup = bs4.BeautifulSoup(req.content.decode('utf-8'),'html.parser')

video_px = soup.find_all(class_="btn btn-download")

co  = 0


for i in video_px:
  co += 1
  c=str(co)
  print('\033[1;32m',c+' . '+'\033[1;33m',i.text)
  print('')

ch=int(input("\033[1;33m[*] \033[1;32;40m Enter Your Choice : \033[1;33m》》》 "))
print('')

if ch == 1:
  link = video_px[ch-1]['href']
  get = requests.get(link)
  save_filename = input('\033[1;32m Enter save file name (Ex-video.mp4) : ')
  print('')
  with open(save_filename,'wb') as f:
    f.write(get.content)
    f.close()
  save()

     
elif ch == 2:
  link = video_px[ch-1]['href']
  get = requests.get(link)
  save_filename = input('\033[1;32m Enter save file name (Ex-video.mp4) : ')
  print('')
  with open(save_filename,'wb') as f:
    f.write(get.content)
    f.close()
  save()

elif ch == 3:
  link = video_px[ch-1]['href']
  get = requests.get(link)
  save_filename = input('\033[1;32m Enter save file name (Ex-video.mp4) : ')
  print('')
  with open(save_filename,'wb') as f:
    f.write(get.content)
    f.close()
  save()
else:
  print('\033[1;31m Please Enter Valid No ')
  print('')
