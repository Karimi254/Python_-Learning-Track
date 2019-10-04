#! /usr/bin/python3.6

#nestedList.py - simple program that shows the utilization of lists within lists.

studDetails = {'Nicholas':{'Jan-April': 60, 'May-August': 65, 'Sept-Dec': 70},
               'Franklin':{'Jan-April': 60, 'May-August':65, 'Sept-Dec': 70},
               'Muna':{'Jan-April': 60, 'May-August': 65, 'Sept-Dec': 70}}

def totalFee(student, semester):
    annualFee = 0
    for k, v in student.items():
        annualFee = annualFee + v.get(semester, 0)
    return annualFee

print('The annual for a JKUAT SSP student is.\n')

print('*Jan-April   ' + str(totalFee(studDetails, 'Jan-April')))
print('*May-August   ' + str(totalFee(studDetails, 'May-August')))
print('*Jan-April   ' + str(totalFee(studDetails, 'Sept-Dec')))

