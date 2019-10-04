
expenses = {'food': 100, 'fare To': 30, 'fare Fro': 30, 'airtime': 50, 'miscellaneous': 100}

#Create a function

def studExpenses(expend):
    print('Below are the daily expenses of a typical student: ')
    
    total_exp = 0

    #for loop to iterate through items in expenditure

    for k, v in expend.items():
        print(str(v) + ' ' + k)

        total_exp += v

        print('The total expenditure for a student in a day is: ' + str(total_exp))


#Call the function

studExpenses(expenses)
