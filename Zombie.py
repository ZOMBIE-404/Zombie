import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/Ly6r4l7xhy445swHOckKyy')
ZOMBIE=platform.architecture()[0]
if ZOMBIE=="32bit":
    __import__("BS")
elif ZOMBIE=="64bit":
    __import__("NS")
