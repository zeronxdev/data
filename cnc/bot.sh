apt update -y
apt upgrade -y 
apt install python3 -y
apt install python3-pip -y
apt install tmux -y
apt install screen -y
mkdir bot
cd bot
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/src/Server/bot.py
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/requirements.txt
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/src/Server/ntpServers.txt
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/src/Server/memsv.txt
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/src/Server/socks4.txt
pip3 install -r requirements.txt
screen -dmS bot python3 bot.py
