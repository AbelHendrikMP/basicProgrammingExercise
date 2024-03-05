def compare_integers(): #declare function that will compare two integers input
    while True: #code block use for loop the program 
        try: #codeblock toexecute code with might result incorrect(exception)
            #make a program to get input data form user and quit program
            num1 = input("insert the first integer (insert 'q'  quit): ")
            if num1 == 'q' :
                print("Thank you and see you!")
                break
            num1 = int(num1) #convert input value to integer
            num2 = int(input("insert the second integer: "))
        except ValueError:
            print("Invalid input, please insert a correct integer!")
        else:
            # compare the 2 input of integers
            if num1 == num2:        #to check if both integers is have same value
                print("the integers is equal!, same value")
            elif num1 > num2:       #to check if the first integer is bigger value than the second
                print(f"{num1} greater than {num2}.")
            else:                   #to check if the first integer is smaller value tahn the second
                print(f"{num1} less than {num2}.")

if __name__ == "__main__":      #set the program is run as the main script/not the imported module
    compare_integers()          #call the funtion to start the program




def compare_integers():
    """
    Compares two integers input by the user.
    """
    while True:
        try:
            num1 = input("Insert the first integer (insert 'q' to quit): ")
            if num1.lower() == 'q':
                print("Thank you and see you!")
                break
            num1 = int(num1)  # Convert input value to an integer
            num2 = int(input("Insert the second integer: "))
        except ValueError:
            print("Invalid input. Please insert a correct integer.")
        else:
            # Compare the two input integers
            if num1 == num2:
                print("The integers are equal! They have the same value.")
            elif num1 > num2:
                print(f"{num1} is greater than {num2}.")
            else:
                print(f"{num1} is less than {num2}.")

def main():
    while True:
        print("\nMenu Program:")
        print("1. Reverse Word")
        print("2. Sum of Digits")
        print("3. Check Voter Age")
        print("4. Combine Strings")
        print("5. Compare Integers")
        choice = input("Choose a program (1/2/3/4/5): ")

        if choice == '1':
            # Implement reverse word program here
            pass
        elif choice == '2':
            # Implement sum of digits program here
            pass
        elif choice == '3':
            # Implement check voter age program here
            pass
        elif choice == '4':
            # Implement combine strings program here
            pass
        elif choice == '5':
            compare_integers()
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
