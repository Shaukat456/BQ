def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def temperature_converter():
    print("Select conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ("1", "2", "3", "4", "5", "6"):
        temp = float(input("Enter the temperature to convert: "))

        if choice == "1":
            print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
        elif choice == "2":
            print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
        elif choice == "3":
            print(f"{temp}°C = {celsius_to_kelvin(temp)}K")
        elif choice == "4":
            print(f"{temp}K = {kelvin_to_celsius(temp)}°C")
        elif choice == "5":
            print(f"{temp}°F = {fahrenheit_to_kelvin(temp)}K")
        elif choice == "6":
            print(f"{temp}K = {kelvin_to_fahrenheit(temp)}°F")
    else:
        print("Invalid Input")


# Run the temperature converter function
temperature_converter()
