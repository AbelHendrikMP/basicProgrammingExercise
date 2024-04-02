user_age = int(input("enter your age: "))

if user_age > 0 and user_age <= 12:
    print("you are a minor\n")
elif user_age >= 13 and user_age <= 19:
    print("you are a teenager\n")
elif user_age >= 20:
    print("you can join our company !\n")
else:
    print("please enter a valid age\n")
    