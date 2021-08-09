#!/data/data/com.termux/files/usr/bin/python
#Function to download profile picture of instagram accounts
from datetime import datetime
import re
import sys,os,base64,time

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

def pp_download():
    
    url = input("\n\033[1;33m Please enter the URL of the profile:")
    print("")
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)
    
    if x:
        check_url1 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/].*\?hl=[a-z-]{2,5}', url)
        check_url2 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com$|^(https:)[/][/]www.([^/]+[.])*instagram.com/$', url)
        check_url3 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/][a-zA-Z0-9_]{1,}$', url)
        check_url4 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/][a-zA-Z0-9_]{1,}[/]$', url)

        if check_url3:
            final_url = url + '/?__a=1'

        if check_url4:
            final_url = url + '?__a=1'

        if check_url2:
            final_url = print("\033[1;31m Please enter an URL related to a profile")
            exit()

        if check_url1:
            alpha = check_url1.group()
            final_url = re.sub('\\?hl=[a-z-]{2,5}', '?__a=1', alpha)
            
    try:
        if check_url3 or check_url4 or check_url2 or check_url1:
            req = requests.get(final_url)
            get_status = requests.get(final_url).status_code
            get_content = req.content.decode('utf-8')

            if get_status == 200:
                print("\n\033[1;32m Downloading the image...")
                find_pp = re.search(r'profile_pic_url_hd\":\"([^\'\" >]+)', get_content)
                pp_link = find_pp.group()
                pp_final = re.sub('profile_pic_url_hd":"', '', pp_link)
                file_size_request = requests.get(pp_final, stream=True)
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
                toolpath="/data/data/com.termux/files/home/All-Downloader"
                path="/sdcard"
                os.chdir(path)
                if os.path.isdir("All-Downloader(SL-Android)")==True:
                    os.chdir('/sdcard/All-Downloader(SL-Android)')
                    if os.path.isdir("INSTAGRAM-IMAGES")==True:
                        os.system('cd INSTAGRAM-IMAGES')
                        if os.path.isdir("Profile-Pictures")==True:
                            os.chdir('/data/data/com.termux/files/home/All-Downloader')
                            os.system("cp"+" "+filename+".jpg"+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-IMAGES/Profile-Pictures")
                            os.system("rm -rf"+" "+filename)
                            print("\033[1;36m Profile picture downloaded successfully")
                        else:
                            os.system("mkdir Profile-Pictures")
                            os.chdir('/data/data/com.termux/files/home/All-Downloader')
                            os.system("cp"+" "+filename+".jpg"+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-IMAGES/Profile-Pictures")
                            os.system("rm -rf"+" "+filename)
                            print("\033[1;36m Profile picture downloaded successfully")
                    else:
                        os.system("mkdir INSTAGRAM-IMAGES")
                        os.system("cd INSTAGRAM-IMAGES")
                        os.system("mkdir Profile-Pictures")
                        os.chdir('/data/data/com.termux/files/home/All-Downloader')
                        os.system("cp"+" "+filename+".jpg"+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-IMAGES/Profile-Pictures")
                        os.system("rm -rf"+" "+filename)
                        print("\033[1;36m Profile picture downloaded successfully")
                else:
                    os.system("mkdir All-Downloader(SL-Android)")
                    os.chdir(fpath)
                    os.system("mkdir INSTAGRAM-IMAGES")
                    os.system("cd INSTAGRAM-IMAGES")
                    os.system("mkdir Profile-Pictures")
                    os.chdir('/data/data/com.termux/files/home/All-Downloader')
                    os.system("cp"+" "+filename+" "+"/sdcard/All-Downloader(SL-Android)/INSTAGRAM-IMAGES/Profile-Pictures")
                    os.system("rm -rf"+" "+filename)
                    print('')
                    print("\033[1;36m Profile picture downloaded successfully.")
                    print('')
                    os.chdir(toolpath)
                    os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
                except Exception:
                    print('\033[1;31m Error !!!')
                    
print('')
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
pp_download()