import os,sys,base64,time

def downH():
	global url
	print("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;36m Compiling Resources...\033[0m\n")
	os.system('echo'+" "+"'--no-mtime -o /sdcard/All-Downloader(SL-Android)/WEB-VIDEO/%(title)s.%(ext)s -f"+" "+'"best[height<=1080]"'+"'"+" "+'> ~/.config/youtube-dl/config')
	print("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;36m Downloading...\033[0m\n")
	os.system("youtube-dl"+" "+url)
	print("File Saved at /sdcard/All-Downloader(SL-Android)/WEB-VIDEO\033[0m")


def downM():
	global url
	print("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;36m Compiling Resources...\033[0m\n")
	os.system('echo'+" "+"'--no-mtime -o /sdcard/All-Downloader(SL-Android)/WEB-VIDEO/%(title)s.%(ext)s -f"+" "+'"136"'+"'"+" "+'> ~/.config/youtube-dl/config')
	print("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;36m Downloading...\033[0m\n")
	os.system("youtube-dl"+" "+url)
	print("File Saved at /sdcard/All-Downloader(SL-Android)/WEB-VIDEO\033[0m")

def downL():
	global url
	print("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;36m Compiling Resources...\033[0m\n")
	os.system('echo'+" "+"'--no-mtime -o /sdcard/All-Downloader(SL-Android)/WEB-VIDEO/%(title)s.%(ext)s -f"+" "+'"397"'+"'"+" "+'> ~/.config/youtube-dl/config')
	print("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;36m Downloading...\033[0m\n")
	os.system("youtube-dl"+" "+url)
	print("File Saved at /sdcard/All-Downloader(SL-Android)/WEB-VIDEO\033[0m")

def downmp3():
	global url
	print("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;36m Compiling Resources...\033[0m\n")
	os.system('echo'+" "+"'--no-mtime -o /sdcard/All-Downloader(SL-Android)/WEB-MP3/%(title)s.%(ext)s -f"+" "+'"best[height<=1080]"'+"'"+" "+'> ~/.config/youtube-dl/config')
	print("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;36m Downloading...\033[0m\n")
	os.system("youtube-dl"+" "+url)
	print("File Saved at /sdcard/All-Downloader(SL-Android)/WEB-MP3\033[0m")



def option():
	global url
	print ("\033[0m\n")
	print ("\033[0m[\033[0m\033[1;34m1\033[0m\033[0m] \033[0m\033[1;93mHigh Resolution\033[0m\n")
	print ("\033[0m[\033[0m\033[1;34m2\033[0m\033[0m] \033[0m\033[1;93mNormal Resolution\033[0m\n")
	print ("\033[0m[\033[0m\033[1;34m3\033[0m\033[0m] \033[0m\033[1;93mLow Resolution\033[0m\n")

	print ("\033[0m[\033[0m\033[1;34m4\033[0m\033[0m] \033[0m\033[1;93mBack to Main Menu\033[0m\n")
	print ("\033[0m\n")
	cho=int(input("\033[1;33m[*] \033[1;32;40m Enter Your Choice : \033[1;33m》》》 "))
	print('')
	if (cho==1):
		downH()
	elif(cho==2):
		downM()
	elif(cho==3):
		downL()
	else:
		print("\033[1;31m Please Enter a Valid number\033[0m ")
		option()


def main():
	print('')
	print("\033[1;33m[1] \033[1;32;40m Download Mp4\033[0m")
	print("\033[1;33m[2] \033[1;32;40m Download Mp3\033[0m")
	print('')
	ch=int(input("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;32;40m Enter Your Choice : \033[1;33m》》》 "))
	print('')
	if (ch==1):
		globals()['url'] = input("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;33m Enter the URL of video :\033[1;35m")
		print("\033[0m")
		option()
	elif(ch==2):
		globals()['url']= input("\033[0m[\033[1;31m*\033[0m\033[0m]\033[1;33m Enter the URL of video :\033[1;35m")
		print("\033[0m")
		option()
	else:
		print("\033[1;31m Please Enter a Valid number \033[0m")
		main()