def check_if_eligible_vote(age):
    """
    Checks if a user's age is between 18 and 65 (inclusive).
    """
    if 18 <= age <= 65:
        return True
    else:
        return False

while True:
    try:
        user_age = int(input("Insert your age (insert 'e' to end the program): "))
        if user_age == 'e':
            print("See you next time!")
            break
        if check_if_eligible_vote(user_age):
            print("You are eligible to vote.")
        else:
            print("You cannot vote.")
    except ValueError:
        print("Invalid input. Please enter your age as an integer.")

