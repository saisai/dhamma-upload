
import os 

def appdata(path):
    print(path)
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            print(os.path.join(root, name))

    for name in dirs:
        print(os.path.join(root, name))


appdata("/c/Users/JCY/AppData/Roaming")
appdata("/c/Users/JCY/AppData/Local")
appdata("/c/Users/JCY/AppData/LocalLow")
#appdata("/cygdrive/c/Users/JCY/AppData/Roaming")
#appdata("/cygdrive/c/Users/JCY/AppData/Local")
#appdata("/cygdrive/c/Users/JCY/AppData/LocalLow")
