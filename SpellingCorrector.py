import json
import enchant
from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter
from difflib import get_close_matches

import subprocess

subprocess.call(["clear"])

f = open("banner.txt","r")
print(f.read())
f.close()


answer = input("[+] press 1 for some text, 2 for a file : ")

data = json.load(open("EnglishWords.json"))

def correctText(text):
    print("*"*78)

    mistakes = 0

    text = text.casefold()
    
    chkr = SpellChecker("en_US",filters=[EmailFilter,URLFilter])
    chkr.set_text(text)

    for err in chkr:
        ww = get_close_matches(err.word,data.keys(),n=5)

        list2String = ", ".join(ww)
        if len(ww) > 0 :
            print("[-] " + err.word + " Is Not an English Word, Do U Mean : " + list2String + " ?")
            mistakes += 1            
        else:
            print("[-] " + err.word + " Is Not an English Word, But I Don't Know What The Fuck Do u Mean")
            mistakes += 1

    if mistakes == 0:
        print("[+] Its All Correct !")
    else:
        print("*"*78)
        print("[-] You Have " + str(mistakes) + " Mistakes !")

            
if answer == "1":
    text = input("[+] Enter some Text : ")

    correctText(text)
    
elif answer == "2":
    file = input("[+] Write The Name Of The Text File Or Its Full Path : ")
    
    import os.path

    if file[-4:] != ".txt":
        file = file + ".txt"
    else:
        file = file
        
    if os.path.isfile(file):
        f = open(file,"r")
        text = f.read()
        correctText(text)
        f.close()
    else:
        print("[-] This File Dosen't Exsist")
    
        
    
    
    

else:
    print("[-] Sorry, Wrong Answer")
