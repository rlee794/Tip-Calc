
#creating a function tip_calc()
def tip_calc():
    bill = float(input("Welcome. How much is the bill for? \n"))
    number = int(input("Thanks, and how many people is the bill going to be split with? \n"))
    tip_percent = float(input ("What percentage are you looking to tip?  No need to enter %.  Just a whole number. \n"))
    total_bill = bill*(1+tip_percent/100)

    if number == 0:
        print("That is not possible!") 
    elif number == 1:
        print("A meal for one!")
        print(f"The total bill is ${round(total_bill,2)}")
    else:
        print(f"The total bill is ${round(total_bill,2)}")
        print(f"Each person should pay ${round(total_bill/number, 2)}")
    return

#running the tip_calc() function
tip_calc()

#giving the user the option to re-run the program
decision = input('Would you like to run the calculator again? (Yes/No) \n')
if decision == 'Yes':
    tip_calc()
elif decision == 'No':
    print("Have a great day!")
else:
    print("Sorry I do not understand!  Have a great day!")
    

