#! /usr/bin/python3.6

""" passwdManager.py - not so secure program that stores account pass"""

PASSWORDS = {'email': 'P9MYTr45EWQmn08L',
       	 'AROMA CAFE': '#password',
	 'linux-user': 'Khsng5Gv',
	 'edx': '$karimi95$',
         'IMEI': 356023081942718 / 68,
         'SerialNo': 'D1AGAS3770137210',
         'wp' : 'virgine2019',
         'USSDIMEI': '*#06#',
         'nicholas.muigai': '$nikki95$',
         'Swahilipot Hub': '5PHm0mb@s@'
         }

import sys, pyperclip

if len(sys.argv) < 2: 
    print('Usage: passwdManager.py [account] - copy account password')
    
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to the clipboard.')

else:
    print('There is no account named ' + account)
