def classify_temperature(temp):
    if temp >= 32:
        return "Hot"
    elif 20 <= temp < 32:
        return "Warm"
    elif 10 <= temp < 20:
        return "Moderate"
    elif 0 <= temp < 10:
        return "Cool"
    else:
        return "Cold"

def main():
    while True:
        try:
            user_input = input("Enter a temperature (in Celsius): ")
            if user_input.lower() == "stop":
                print("Exiting the program. Have a great day!")
                break

            temperature = float(user_input)
            classification = classify_temperature(temperature)
            print(f"The temperature is classified as: {classification}")
        except ValueError:
            print("Invalid input. Please enter a valid numeric temperature or 'stop' to exit.")

if __name__ == "__main__":
    main()

