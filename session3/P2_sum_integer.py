# def sum_of_digits(n):
#     """
#     Calculates the sum of digits in a given integer.
#     """
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit
#         n //= 10
#     return total

# # Example usage
# number = int(input("Enter an integer: "))
# result = sum_of_digits(number)
# print(f"The sum of digits in {number} is {result}.")




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

while True:
    try:
        number = input("Enter an integer (insert 'e' to end the program): ")
        if number == 'e':
            print("See you next time!")
            break
        number = int(number)
        result = sum_of_digits(number)
        print(f"The sum of digits in {number} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")

