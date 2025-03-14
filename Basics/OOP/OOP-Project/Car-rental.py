# Parent Class
class Vehicle:
    def __init__(self, brand, model, rental_price):
        self.brand = brand
        self.model = model
        self.rental_price = rental_price

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Rental Price: ${self.rental_price}/day"


# Child Class: Car (Inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, rental_price, num_doors):
        super().__init__(brand, model, rental_price)
        self.num_doors = num_doors

    def display_info(self):  # Polymorphism: Different implementation
        return f"{super().display_info()}, Doors: {self.num_doors}"


# Child Class: Bike (Inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, brand, model, rental_price, has_helmet):
        super().__init__(brand, model, rental_price)
        self.has_helmet = has_helmet

    def display_info(self):  # Polymorphism: Different implementation
        helmet_info = "Yes" if self.has_helmet else "No"
        return f"{super().display_info()}, Helmet Included: {helmet_info}"


# Creating instances
car1 = Car("Toyota", "Corolla", 50, 4)
bike1 = Bike("Honda", "CBR500", 30, True)

# Polymorphism: Same method, different behaviors
vehicles = [car1, bike1]
for v in vehicles:
    print(v.display_info())  # Calls overridden methods


# Parent Class
class Vehicle:
    def __init__(self, brand, model, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.available = True  # Availability status

    def display_info(self):
        status = "Available" if self.available else "Rented"
        return (
            f"{self.brand} {self.model} - ${self.rental_price_per_day}/day [{status}]"
        )

    def rent_vehicle(self):
        if self.available:
            self.available = False
            return True
        return False


# Child Class: Car (Inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, rental_price_per_day, num_doors):
        super().__init__(brand, model, rental_price_per_day)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, Doors: {self.num_doors}"


# Child Class: Bike (Inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, brand, model, rental_price_per_day, has_helmet):
        super().__init__(brand, model, rental_price_per_day)
        self.has_helmet = has_helmet

    def display_info(self):
        helmet_info = "Yes" if self.has_helmet else "No"
        return f"{super().display_info()}, Helmet Included: {helmet_info}"


# Rental Management System
class RentalSystem:
    def __init__(self):
        self.vehicles = []  # List of available vehicles

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_available_vehicles(self):
        print("\nAvailable Vehicles:")
        for idx, vehicle in enumerate(self.vehicles):
            if vehicle.available:
                print(f"{idx + 1}. {vehicle.display_info()}")

    def rent_vehicle(self, index):
        if 0 <= index < len(self.vehicles):
            vehicle = self.vehicles[index]
            if vehicle.rent_vehicle():
                print(
                    f"\n✅ You have successfully rented the {vehicle.brand} {vehicle.model}."
                )
            else:
                print("\n❌ Sorry, this vehicle is already rented.")
        else:
            print("\n⚠️ Invalid selection!")


# Main program
def main():
    rental_system = RentalSystem()

    # Adding sample vehicles
    rental_system.add_vehicle(Car("Toyota", "Corolla", 50, 4))
    rental_system.add_vehicle(Car("Honda", "Civic", 55, 4))
    rental_system.add_vehicle(Bike("Yamaha", "YZF-R3", 30, True))
    rental_system.add_vehicle(Bike("Harley", "Iron 883", 40, False))

    while True:
        print("\n🚗 Vehicle Rental System")
        print("1. View Available Vehicles")
        print("2. Rent a Vehicle")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rental_system.display_available_vehicles()
        elif choice == "2":
            rental_system.display_available_vehicles()
            index = int(input("Enter vehicle number to rent: ")) - 1
            rental_system.rent_vehicle(index)
        elif choice == "3":
            print("\n👋 Thank you for using the Vehicle Rental System!")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()


# 🚗 Vehicle Rental System
# 1. View Available Vehicles
# 2. Rent a Vehicle
# 3. Exit
# Enter your choice: 1

# Available Vehicles:
# 1. Toyota Corolla - $50/day [Available], Doors: 4
# 2. Honda Civic - $55/day [Available], Doors: 4
# 3. Yamaha YZF-R3 - $30/day [Available], Helmet Included: Yes
# 4. Harley Iron 883 - $40/day [Available], Helmet Included: No

# Enter your choice: 2
# Enter vehicle number to rent: 2

# ✅ You have successfully rented the Honda Civic.

# 🚗 Vehicle Rental System
# 1. View Available Vehicles
# 2. Rent a Vehicle
# 3. Exit
# Enter your choice: 1

# Available Vehicles:
# 1. Toyota Corolla - $50/day [Available], Doors: 4
# 2. Yamaha YZF-R3 - $30/day [Available], Helmet Included: Yes
# 3. Harley Iron 883 - $40/day [Available], Helmet Included: No
