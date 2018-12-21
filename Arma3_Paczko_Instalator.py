import json
import time
import sys
import os
import wget
import shutil
dir_path = os.path.dirname(os.path.realpath(__file__))

wget.download("https://github.com/Hubix9/Arma-3-Mod-Collections/releases/download/Var/vars.json")
jsonfile = open(os.path.join(dir_path,"vars.json"))
jsondata = json.load(jsonfile)
jsonfile.close()
os.remove(os.path.join(dir_path,"vars.json"))

localappdatapath = os.path.expandvars("%LOCALAPPDATA%")

def init():
    os.system('cls')
    print("==================================")
    print("==================================")
    print("Dostepne opcje:")
    lul = 0
    for option in jsondata:
        print(str(lul) + ": " + jsondata[lul]["text"])
        lul = lul + 1
    print(str(lul) + ": wyjdz\n")
    paczka = input("Jaka opcje chcesz wybrac?: ")
    print("\n")
    temp = float(paczka)
    temp = int(temp) 
    if (temp == lul):
        sys.exit(0)
    wget.download(jsondata[int(float(paczka))]["Url"])
    tmp = float(paczka)
    tmp = int(tmp)
    tmp = jsondata[tmp]["Url"].split("/")
    tmp = tmp[len(tmp) - 1]
    srcpath = os.path.join(dir_path, tmp)
    dstpath = os.path.join(localappdatapath,"Arma 3 Launcher","Presets",tmp)
    shutil.copy(srcpath,dstpath)
    os.remove(srcpath)
    print("\n\n=================================")
    print("\npaczka zostala wgrana pomyslnie")
    print("\n================================")
    time.sleep(3)
    init()

init()

