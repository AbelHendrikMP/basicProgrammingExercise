def check_number_even_and_greater_than_10(): #make
    while True:
        try:
            print("this program is to check of your input is even and greater than 10!") 
            num1 = input("please insert the integers to check(insert 'e' to exit): ")

            if num1 == 'e' :
                print("thank you and see you soon master!")
                break

            num1=int(num1)
        except ValueError:
            print("please enter the correct integer input! \n")
        else:
            #check the number if even and greater than 10
            if num1 % 2 == 0 and num1> 10 :
                print(f"your input {num1} is accepted, congrats!\n " )
            elif num1 == 10 :
                print(f"your input {num1} is equal with 10, not greater than 10, re-try\n")
            elif num1 % 2 == 0 and num1 < 10:
                print(f"your input {num1} is even number, but less than 10, re-try\n")
            else:
                print(f"your input {num1} is greater than 10, but still not even number, re-try\n")

if __name__== "__main__" :
    check_number_even_and_greater_than_10()

