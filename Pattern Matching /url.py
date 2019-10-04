#! /usr/bin/python3.6

import re

urls = '''
https://www.kenya.org
http://virginexplorers.com
https://www.wakanda.com
https://nasa.net

'''

# pattern = re.compile(r'https?://(www\.)?(
# \w+)(\.w+)')
pattern = re.compile(r'https?://(www\.)?\w+\.(org|com|net)')

mo = pattern.finditer(urls)

for res in mo:
    print(res)
