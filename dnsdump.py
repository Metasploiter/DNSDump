#!/usr/bin/python3
import os
import sys
import banner
import socket
from termcolor import colored
import colorama
colorama.init()
list_location = str(os.path.dirname(__file__)) + '/domainlist.txt'
def check_domain_list():
    if os.path.exists(list_location) or os.path.exists('domain.txt'):
        pass
    else:
        print('domain list file doesn\'t exists !')
        sys.exit()
check_domain_list()
print(colored(banner.banner1,'red'))
target_domain = str(input('Enter target domain: '))
print('\n')
count = 0
domain_list = open(list_location,'r')
for domain in domain_list.readlines():
    subdomain = str(domain.replace('\n','')) +'.'+ target_domain
    try:
        print('[+]',subdomain,'Has Address',socket.gethostbyname(subdomain))
        count += 1
    except:
        pass
print('\n[*] Founded ',count)
