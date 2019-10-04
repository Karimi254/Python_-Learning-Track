#! /usr/bin/python3.6

""" passwdManager.py - not so secure program that stores account pass"""

PASSWORDS = {'email': '',
       	 'AROMA CAFE': '',
	 'linux-user': '',
	 'Swahilipot Hub': ''
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
