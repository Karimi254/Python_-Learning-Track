#! /usr/bin/python3.6

def pLangRating(ratingDict, left, right):

    #Print the title first, centered
    print('PROGRAMMING LANGUAGES POPULARITY RATING'.center(left + right, '+'))

    #Loop through the ratingDict using for loop
    for k, v in ratingDict.items():
        print(k.ljust(left, '.') + str(v).rjust(right))

      


#Populate the ratingDict

pLang = {'Python': str(96)+'%', 'PHP': str(90)+'%', 'C': str(94)+'%', 'Ruby': str(78)+'%', 'C++': str(84)+'%'}
pLangRating(pLang, 18, 4)
pLangRating(pLang, 30, 6)

