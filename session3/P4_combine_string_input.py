def concatenate_strings(str1, str2):
    """
    combine 2 string and return the result.
    """
    return str1 + str2


def main():
    while True:
        try:
            string1 = input("insert the first string input (press 'q' for quit)): ")
            if string1.lower() == 'q':
                break
            string2 = input("insert the second string input: ")
            result = concatenate_strings(string1, string2)
            print(f"the result  of combined string input is: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
