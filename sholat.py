import requests
import json
import time
import sys
import os
import platform
def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

clear()
location = input("Ketik Lokasi Anda Lalu ENTER, Contoh: jakarta??"+"\n")
req = requests.get('https://time.siswadi.com/pray/'+location)
st = json.loads(req.content)
dat = (st["data"])
subuh = (dat["Fajr"])
duhur = (dat["Dhuhr"])
asar = (dat["Asr"])
magrib = (dat["Maghrib"])
isya = (dat["Isha"])

echo "************************************************"
print ("Info Time "+str(time.strftime('%a, %d %B %Y | %H:%M:%S')))
print("Jadwal Sholat Hari Ini Di "+location)
echo "************************************************"
echo " "
print ("Subuh   : "+subuh+"\n")
print ("Dzuhur  : "+duhur+"\n")
print ("Ashar   : "+asar+"\n")
print ("Mahgrib : "+magrib+"\n")
print ("Isya    : "+isya+"\n")
