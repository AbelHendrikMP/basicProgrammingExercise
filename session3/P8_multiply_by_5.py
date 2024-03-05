 
def calculate_multiply_by_5(num):
    """
    multiplying any value with 5
    """
    return num * 5

def main():
    while True:
        try:
            num = input("insert lenght of Square (press 'q' for quit): ")
            if num.lower() == 'q':
                break
            num = int(num)  # turn input in to integer
            calculate = calculate_multiply_by_5(num)
            print(f"inserted input {num} multiplied by 5 is {calculate}.")
        except ValueError:
            print("invalid input. you must insert the valid input (positive integers)." )

if __name__ == "__main__":
    main()

 