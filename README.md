# backupscript
this will search for tarball files(-o) recursively (tar.gz) and download them to your specified local path directory(-t)
# Installation
sudo wget -O /usr/local/bin/backupscript https://raw.githubusercontent.com/mojjoGh/backupscript/master/backupscript.py
sudo chmod +x /usr/local/bin/backupscript

# Sample Usage
backupscript -a ipa.ddr.ess -u root -i rsa_vps -o /home/ -t /home/localuser/py
