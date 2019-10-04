#! /usr/bin/python3.6

import re
text_search = '''
    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ

    nicholas.com

    254-710-568-014
    254-775-539-7750

    Mr. Nicholas
    Mr Corey
    Ms. Hezna
    Mrs. Wambui
    Mr. T
    Ms Davis

    '''

# pattern = re.compile(r'\d\d\d.\d\d\d-\d\d\d.\d\d\d\d')
# using quantifiers to match
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

mo = pattern.finditer(text_search)
for result in mo:
    print(result)
