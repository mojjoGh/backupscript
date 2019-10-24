# backupscript

# Installation
sudo wget -O /usr/local/bin/backupscript https://raw.githubusercontent.com/mojjoGh/backupscript/master/backupscript.py
sudo chmod +x /usr/local/bin/backupscript

# Sample Usage
backupscript -a 192.168.1.21 -u user -i id_rsa -o /home/user/ -t /home/localuser/py
