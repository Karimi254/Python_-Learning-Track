#! /usr/bin/python3.6

#Introduction to pattern Matching

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

#print(isPhoneNumber('254-710-5680'))

message = ('Call me at 071-056-8014 tomorrow. 071-056-8888 is my office. ')
for m in range(len(message)):
    chunk = message[m:m+12]
    if isPhoneNumber(chunk):
        print('Phone number found ' + chunk)
print ('Done')
