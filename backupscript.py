#!/usr/bin/env python3
from subprocess import call, check_output, Popen, PIPE
import argparse, os

def get_arguments():
    # return "hello"
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--address', type=str, metavar='', required=True, help="Required: server ip address")
    parser.add_argument('-u','--user', type=str, metavar='', required=True, help="Required: server user account")
    parser.add_argument('-i','--rsa', type=str, metavar='', required=True, help="Required: user RSA key")
    parser.add_argument('-o','--origin', type=str, metavar='', required=True, help="Required: where the origin of the files")
    parser.add_argument('-t','--to', type=str, metavar='', required=True, help="Required: where the destination of the files")
    options = parser.parse_args()
    if not options.address:
        parser.error('[-] Please specify an address, use --help for more info')
    elif not options.user:
        parser.error('[-] Please specify a user associated to the server, use --help for more info') 
    elif not options.rsa:
        parser.error('[-] Please specify an absolute path for RSA Key, use --help for more info') 
    elif not options.origin:
        parser.error('[-] Please specify the origin of the files/directories, use --help for more info') 
    elif not options.to:
        parser.error('[-] Please specify the location where destination of the files/directories, use --help for more info') 
    return options
    # group
    # parser.add_argument('-h','--help', hel)

def pull_data(options):
    # args = '-av -e "ssh -i /home/sysadmin/.ssh/id_rsa" root@192.168.43.136:~/hey.txt $(pwd)'
    #print(options)
    args = '-av -m --include="*.tar.gz" --include="*/" --exclude="*" --exclude ".*/" -e "ssh -i '+options.rsa+'" '+options.user+'@'+options.address+':'+options.origin+' '+options.to
    print(args)
    exec_bash = Popen('rsync ' + args, shell=True,stdout=PIPE, stdin=PIPE, stderr=PIPE)
    while True:
        o = exec_bash.stdout.readline()
        if o == '' or exec_bash.poll() != None:
            print("if root",o.decode())
            break
        elif "failed:" in o.decode():
            print("No such file/directory")
            break
        else:
            print("else output",o.decode())
            
    return options.origin,options.to,options.user

if __name__ == '__main__':
    options = get_arguments()
    options = pull_data(options)
    #print(options[0])
    # for opt in options:
    #     print(opt)
    

