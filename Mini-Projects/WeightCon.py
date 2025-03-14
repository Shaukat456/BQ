def kilograms_to_grams(kilograms):
    return kilograms * 1000


def grams_to_kilograms(grams):
    return grams / 1000


def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462


def pounds_to_kilograms(pounds):
    return pounds / 2.20462


def weight_converter():
    print("Select conversion:")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        weight = float(input("Enter the weight to convert: "))

        if choice == "1":
            print(f"{weight} kg = {kilograms_to_grams(weight)} g")
        elif choice == "2":
            print(f"{weight} g = {grams_to_kilograms(weight)} kg")
        elif choice == "3":
            print(f"{weight} kg = {kilograms_to_pounds(weight)} lbs")
        elif choice == "4":
            print(f"{weight} lbs = {pounds_to_kilograms(weight)} kg")
    else:
        print("Invalid Input")


# Run the weight converter function
weight_converter()
