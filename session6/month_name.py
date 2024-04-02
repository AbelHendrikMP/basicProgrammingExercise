while True:    
    month = int(input("enter the month number 1-12!, 0 to stop:  "))
    if  month == 0 :
        break
    elif 0<month<=12:
        if month == 1:
            print("the 1st month is JANUARY!\n ")
        elif month == 2:
            print("The 2nd month is FEBRUARY!\n ")
        elif month == 3: 
            print("The 3rd month is MARCH!\n ")
        elif month == 4: 
            print("The 4th month is APRIL!\n ")
        elif month == 5: 
            print("The 5th month is MEI!\n ")
        elif month == 6: 
            print("The 6th month is JUNE!\n ")
        elif month == 7: 
            print("The 7th month is JULY!\n ")
        elif month == 8: 
            print("The 8th month is AUGUST!\n ")    
        elif month == 9: 
            print("The 9th month is SEPTEMBER!\n ")
        elif month == 10: 
            print("The 10th month is OCTOBER!\n ")
        elif month == 11: 
            print("The 11th month is NOVEMBER!\n ")
        elif month ==12: 
            print("The 12th month is DECEMBER!\n ")
    else:
        print("Invalid input! Please enter a number between 1 and 12.")
print("the program has stopped, SEE YOU !\n")