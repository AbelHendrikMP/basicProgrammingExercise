def reverse_word(word):
    return word[::-1]

def sum_of_digits(n):
    """
    Calculates the sum of digits in a given integer.
    """
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

def check_if_eligible_vote(age):
    """
    Checks if a user's age is between 18 and 65 (inclusive).
    """
    if 18 <= age <= 65:
        return True
    else:
        return False

def concatenate_strings(s1, s2):
    """
    Concatenates two strings.
    """
    return s1 + s2

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

def check_number_even_and_greater_than_10():
    """
    Checks if a user's input is even and greater than 10.
    """
    while True:
        try:
            print("This program checks if your input is even and greater than 10!")
            num1 = input("Please insert an integer (insert 'e' to exit): ")

            if num1.lower() == 'e':
                print("Thank you and see you soon!")
                break

            num1 = int(num1)
        except ValueError:
            print("Please enter a valid integer input.")
        else:
            # Check if the number is even and greater than 10
            if num1 % 2 == 0 and num1 > 10:
                print(f"Your input {num1} is accepted. Congratulations!\n")
            elif num1 == 10:
                print(f"Your input {num1} is equal to 10, not greater than 10. Please re-try.\n")
            elif num1 % 2 == 0 and num1 < 10:
                print(f"Your input {num1} is an even number, but less than 10. Please re-try.\n")
            else:
                print(f"Your input {num1} is greater than 10, but still not an even number. Please re-try.\n")

def count_characters():
    """
    Counts the number of characters in a user-input string.
    """
    user_input = input("Please enter a string: ")
    character_count = len(user_input)
    print(f"The number of characters in your input is: {character_count}")

def calculate_multiply_by_5(num):
    """
    Mengalikan nilai apa pun dengan 5.
    """
    return num * 5

def age_classifier():
    """
    Classifies a person's age group based on input.
    """
    try:
        age = int(input("Enter your age: "))
        if age >= 21:
            print("Welcome! You are accepted because you are at least 21 years old.")
        else:
            print("Unfortunately, you cannot join us. You must be at least 21 years old.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

def extract_domain(email):
    """
    Extracts the domain name from an email address.
    """
    return email.split('@')[1]

def calculate_area_of_square(side):
    """
    Calculates the area of a square given its side length.
    """
    return side ** 2

def main():
    while True:
        print("\nMenu Program:")
        print("1. Run reverse word program")
        print("2. Run sum of digit program")
        print("3. Run check voter age program")
        print("4. Combine Strings program")
        print("5. Compare integers program")
        print("6. check if integer is even and greater than 10 program")
        print("7. characters counter program")
        print("8. multiply value by 5 program")
        print("9. Age Classifier program")
        print("10. Extract Domain from Email program")
        print("11. Calculate Area of a Square")

        print("12. Exit")
        choice = input("choose program (1/2/3/4/5/6/7/8/9/10/11/12): ")

        if choice == '1':
            word = input("Enter a word: ")
            print(f"Reversed word: {reverse_word(word)}")
        elif choice == '2':
            number = int(input("Enter an integer: "))
            print(f"The sum of digits in {number} is {sum_of_digits(number)}.")
        elif choice == '3':
            user_age = int(input("Enter your age: "))
            if check_if_eligible_vote(user_age):
                print("You are eligible to vote.")
            else:
                print("You cannot vote.")
        elif choice == '4':
                string1 = input("Enter the first string: ")
                string2 = input("Enter the second string: ")
                result = concatenate_strings(string1, string2)
                print(f"The combined string is: {result}")
        elif choice == '5':
            compare_integers()
        elif choice == '6':
            check_number_even_and_greater_than_10()
        elif choice == '7':
            count_characters()
        elif choice == '8':
            try:
                num = int(input("Enter the length of a square's side (type 'q' to quit): "))
                result = calculate_multiply_by_5(num)
                print(f"The result of multiplying {num} by 5 is {result}.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        elif choice == '9':
            age_classifier()
        elif choice == '10':
            try:
                email = input("Enter your email address: ")
                domain = extract_domain(email)
                print(f"The extracted domain name: {domain}")
            except IndexError:
                print("Invalid email format. Please enter a valid email address.")
        elif choice == '11':
            try:
                side = float(input("Enter the length of a square's side: "))
                area = calculate_area_of_square(side)
                print(f"The area of the square with side length {side} is {area}.")
            except ValueError:
                print("Invalid input. Please enter a valid positive number.")
        
        elif choice == '12':
            print("Terima kasih telah menggunakan program pengendali!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
