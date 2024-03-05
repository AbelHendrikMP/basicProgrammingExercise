# length = int(input("insert the lenght: "))
# area = length ** 2

def calculate_area_of_square(lenght):
    """
    Menghitung luas persegi berdasarkan panjang sisi.
    """
    return lenght ** 2

def main():
    while True:
        try:
            lenght = input("insert lenght of Square (press 'q' for quit): ")
            if lenght.lower() == 'q':
                break
            lenght = float(lenght)  # turn input in to integer
            area = calculate_area_of_square(lenght)
            print(f"area of square with the length {lenght} is {area}.")
        except ValueError:
            print("invalid input. you must insert the valid input (positive integers)." )

if __name__ == "__main__":
    main()

 