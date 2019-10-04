#! /usr/bin/python3.6

import re

emails = '''

NicholasKarimi.dev@gmail.com
nicmuigai17@yahoo.net
info@karimi.org
'''

# pattern = re.compile(r'[a-zA-Z0-9.]+@[a-z]+\.(com|net|org)')
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

mo = pattern.finditer(emails)

for match in mo:
    print(match)
