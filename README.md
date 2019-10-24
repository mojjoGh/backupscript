# backupscript
this will search for tarball files(-o) recursively (tar.gz) and download them to your specified local path directory(-t)
# Installation
sudo wget -O /usr/local/bin/backupscript https://raw.githubusercontent.com/mojjoGh/backupscript/master/backupscript.py
sudo chmod +x /usr/local/bin/backupscript
# Manual
backupscript --help
usage: backupscript [-h] -a  -u  -i  -o  -t

optional arguments:
  -h, --help       show this help message and exit
  -a , --address   Required: server ip address
  -u , --user      Required: server user account
  -i , --rsa       Required: user RSA key
  -o , --origin    Required: where the origin of the files
  -t , --to        Required: where the destination of the files
# Sample Usage
backupscript -a ipa.ddr.ess -u root -i rsa_vps -o /home/ -t /home/localuser/py
