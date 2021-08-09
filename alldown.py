#!/data/data/com.termux/files/usr/bin/python
import os,time,base64,sys

try:
    from tqdm import tqdm
    import requests
    from colorama import Fore,init,Style
    from urllib import request
    os.system("pkg install wget")
    os.system("clear")
    print("")
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

def updateA():
    if os.path.exists("version.txt"):
        file=open('version.txt','r')
        vr=file.read()
        file.close()
        file=open('temp.txt','w')
        file.write(vr)
        file.close()
        os.system("rm -rf version.txt")

        os.system("wget -L https://raw.githubusercontent.com/RazorKenway/All-Downloader/main/version.txt")
        file=open('version.txt','r')
        VR=file.read()
        file.close()

        file=open('temp.txt','r')
        vr=file.read()
        file.close()
        os.system("clear")
        if(VR==vr):
            print('')
            main()
        else:
            print('')
            print("\033[1;31;40m New Version Available !!\n\n")
            print("\033[1;32m Updating Please Wait....\n\n")
            update()
    else:
    
        os.system("touch version.txt")
        file=open('version.txt','r')
        vr=file.read()
        file.close()
        file=open('temp.txt','w')
        file.write(vr)
        file.close()
        os.system("rm -rf version.txt")

        os.system("wget -L https://raw.githubusercontent.com/RazorKenway/All-Downloader/main/version.txt")
        file=open('version.txt','r')
        VR=file.read()
        file.close()

        file=open('temp.txt','r')
        vr=file.read()
        file.close()
        os.system("clear")
        if(VR==vr):
            print('')
            main()
        else:
            print('')
            print("\033[1;31;40m New Version Available !!\n\n")
            print("\033[1;32m Updating Please Wait....\n\n")
            update()    
def Spinner():
    l=['|','/','-','\\']
    for i in l+l+l:
        sys.stdout.write('\r'+Style.BRIGHT+Fore.LIGHTYELLOW_EX+'[*] Checking Your Internet Connection  '+i)
        sys.stdout.flush()
        time.sleep(0.2)

        

def update():
    os.system("mv update.py $HOME")
    os.chdir("/data/data/com.termux/files/home")
    os.system("python update.py")



def main():
    print("\033[90m                █████╗ ██╗     ██╗   ")
    print("\033[90m               ██╔══██╗██║     ██║")
    print("\033[90m               ███████║██║     ██║")
    print("\033[90m               ██╔══██║██║     ██║")
    print("\033[90m               ██║  ██║███████╗███████╗")
    print("\033[0m               ╚═╝  ╚═╝╚══════╝╚══════╝")

    print("\033[33m       ██████╗  █████╗  ██╗       ██╗███╗  ██╗")
    print("\033[33m       ██╔══██╗██╔══██╗ ██║  ██╗  ██║████╗ ██║")
    print("\033[33m       ██║  ██║██║  ██║ ╚██╗████╗██╔╝██╔██╗██║")
    print("\033[33m       ██║  ██║██║  ██║  ████╔═████║ ██║╚████║")
    print("\033[33m       ██████╔╝╚█████╔╝  ╚██╔╝ ╚██╔╝ ██║ ╚███║")
    print("\033[0m       ╚═════╝  ╚════╝    ╚═╝   ╚═╝  ╚═╝  ╚══╝")
    print("")
    print("\033[1;31m               Tool By Razor Kenway\033[0m")
    print("\033[1;32;37m               SL Android Srilanka\033[0m")
    bar = "\033[1;36m\n__________________________________________________________\n"
    print (bar)
    print("\033[1;33m[1] \033[1;32;40mFaceBook  Video        \033[1;33m[8] \033[1;32;40mPorn Hub")
    print("\033[1;33m[2] \033[1;32;40mYouTube   Video/MP3    \033[1;33m[9] \033[1;32;40mBrazzers")
    print("\033[1;33m[3] \033[1;32;40mInstagram Video/Img    \033[1;33m[10] \033[1;32;40mAny Porn Site")
    print("\033[1;33m[4] \033[1;32;40mInstagram Profile Pic  \033[1;33m[11] \033[1;36mSubscribe Us")
    print("\033[1;33m[5] \033[1;32;40mPinterest Video        \033[1;33m[12] \033[1;36mUpdate Tool")
    print("\033[1;33m[6] \033[1;32;40mTwitter   Video")
    print("\033[1;33m[7] \033[1;32;40mAll-Web Video/MP3      \033[1;33m[0] \033[1;31mExit")
    print("")
    ch=int(input("\033[1;33m[*] \033[1;32;40m Enter Your Choice : \033[1;33m》》》 "))
    print("")
    binpath=".bin/.temp/.var/.usr/.cd/.tmp/.usd/.data/.data/.data/.data/.data/.temp"
    if (ch==1):
        os.chdir(binpath)
        os.system("python .fb.py")
    elif(ch==2):
        os.chdir(binpath)
        os.system("python .youtube.py")
    elif(ch==3):
        os.chdir(binpath)
        os.system("python .insta.py")
    elif(ch==4):
        os.chdir(binpath)
        os.system("python .instaprof.py")
    elif(ch==5):
        os.chdir(binpath)
        os.system("python .pinterest.py")
    elif(ch==6):
        os.chdir(binpath)
        os.system("python .twitter.py")
    elif(ch==7):
        os.chdir(binpath)
        os.system("python .web.py")        
    elif(ch==8):
        os.chdir(binpath)
        os.system("python .web.py")
    elif(ch==9):
        os.chdir(binpath)
        os.system("python .web.py")
    elif(ch==10):
        os.chdir(binpath)
        os.system("python .web.py")
    elif(ch==11):
        os.system("termux-open-url https://www.youtube.com/channel/UCLJPOlgldE496tVZjSRi45Q")
    elif(ch==12):
        update()      
    elif(ch==0):
        sys.exit()
    else:
        print("\033[1;31m Please Enter a Valid number ")
        main()
print('')
try:
    Spinner()
    request.urlopen('https://httpbin.org/get')
    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+'\n[+] Connection Successful !')
    print('')
    updateA()
except:
    time.sleep(0.4)
    print(Fore.LIGHTRED_EX+Style.BRIGHT+'\n[!] You Aren\'t Connected To Internet !')
    time.sleep(0.3)
    print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Please Connect To Internet To Continue...')
    time.sleep(0.3)
    exit()    

