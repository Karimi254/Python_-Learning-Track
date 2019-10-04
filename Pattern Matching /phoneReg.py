
#! /usr/bin/python3.6

import re


# phoneReg = re.compile(r'''(
#         (\d{3}|\(d{3}\))?       				#area code
#         (\s|-|\.)?              				#seperator
#         \d{3}                   				#first 3 digits
#         (\s|-|\.)               				#seperator
#         \d{4}                  				        #last 4 digits
#         (\s*(ext|x|ext.)\s*\d(2,5)? 			        #extension

#         )''', re.VERBOSE)

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                      #area code
(\s|-|\.)?                              #seperator                           
(\d{3})                                 #first 3 digits
(\s|-|\.)                               #seperator
(\d{4})                                 #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?          #extensions
)''', re.VERBOSE)


phoneReg = re.compile(r'(\d{3}|\(d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s$\d(2, 5)?')

mo = phoneReg.search('My phone number is 254-710-5680 and home is (710)-568-0142')

mo.group(1)
