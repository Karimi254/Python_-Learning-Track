#! /usr/bin/python3.6

#This programs users the pyperclip module, copies text from wiki and adds bullets to it.

import pyperclip

text = pyperclip.paste()

lines = tetx.split('\n')

for i in range (len(lines)):
    lines[i] = "*" + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
