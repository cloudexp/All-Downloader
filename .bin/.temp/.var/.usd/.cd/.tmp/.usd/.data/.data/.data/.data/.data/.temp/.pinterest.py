#!/data/data/com.termux/files/usr/bin/python
import requests,bs4,os,base64,time,sys

url = "https://pinterestvideodownloader.com/"
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


parm = {
"url":input("\n\n\033[1;33m Enter Pinterest Video URL :")
}
print('')
head = {
"Host": "pinterestvideodownloader.com",
"Connection": "keep-alive",
"Content-Length": "34",
"Cache-Control": "max-age=0",
"Origin": "https://pinterestvideodownloader.com",
"Upgrade-Insecure-Requests":"1",
"DNT": "1",
"Content-Type": "application/x-www-form-urlencoded",
"Save-Data":"on",
"User-Agent":"Mozilla/5.0 (Linux; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"navigate",
"Sec-Fetch-User":"?1",
"Sec-Fetch-Dest":"document",
"Referer": "https://pinterestvideodownloader.com/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language": "si,en;q=0.9,en-US;q=0.8,en-GB;q=0.7",
"Cookie": "__gads=ID=f047ab66f3fce759-22e5c944fac9003c:T=1624589047:RT=1624589047:S=ALNI_MZPGagvknBF3UnBcfieuRzl7r3zxQ; _ga=GA1.2.1059175299.1624589047; _gid=GA1.2.349244392.1624589050; _gat_gtag_UA_178031006_1=1"
}


soup = bs4.BeautifulSoup(requests.post(url,parm,headers=head).content.decode('utf-8'),"html.parser")

url = soup.find_all("source")[0]['src']
head2 = {
"Host":"v.pinimg.com",
"Connection":"keep-alive",
"DNT":"1",
"Accept-Encoding":"identity;q=1, *;q=0",
"Save-Data":"on",
"User-Agent":"Mozilla/5.0 (Linux; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
"Accept":"*/*",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"no-cors",
"Sec-Fetch-Dest":"video",
"Referer": url,
"Accept-Language": "si,en;q=0.9,en-US;q=0.8,en-GB;q=0.7",
"Range":"bytes=0-"

}
save_filename = input('\n\033[1;33m Enter save file name (Ex-video.mp4) :')
print('')
with open(save_filename,"wb") as f:
     f.write(requests.get(url,headers=head2).content)

fpath="/sdcard/All-Downloader(SL-Android)"
toolpath="/data/data/com.termux/files/home/All-Downloader"
path="/sdcard"
os.chdir(path)
if os.path.isdir("All-Downloader(SL-Android)")==True:
    os.chdir('/sdcard/All-Downloader(SL-Android)')
    if os.fpath.isdir("PINTEREST-VIDEO")==True:
    
        os.chdir('/data/data/com.termux/files/home/All-Downloader')
        os.system("cp"+" "+save_filename+" "+"/sdcard/All-Downloader(SL-Android)/PINTEREST-VIDEO")
        os.system("rm -rf"+" "+save_filename)
        print('')
        print("\033[1;36m Video downloaded successfully.")
        print('')
        os.chdir(toolpath)
        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
    else:
        
        os.system("mkdir PINTEREST-VIDEO")
        os.chdir('/data/data/com.termux/files/home/All-Downloader')
        os.system("cp"+" "+save_filename+" "+"/sdcard/All-Downloader(SL-Android)/PINTEREST-VIDEO")
        os.system("rm -rf"+" "+save_filename)
        print('')
        print("\033[1;36m Video downloaded successfully.")
        print('')
        os.chdir(toolpath)
        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
else:
    os.system("mkdir All-Downloader(SL-Android)")
    os.chdir(fpath)
    os.system("mkdir PINTEREST-VIDEO")
    os.chdir('/data/data/com.termux/files/home/All-Downloader')
    os.system("cp"+" "+save_filename+" "+"/sdcard/All-Downloader(SL-Android)/PINTEREST-VIDEO")
    os.system("rm -rf"+" "+save_filename)
    print('')
    print("\033[1;36m Video downloaded successfully.")
    print('')
    os.chdir(toolpath)
    os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")