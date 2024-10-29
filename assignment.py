# exercises related to nested functions with code

# 1) What is the output of the following code?

bicycles = ["trek", "cannondale", "redline", "specialized"]

cars = ["audi", "bmw", "subaru", "toyota"]

vehicles = [bicycles, cars]

print(vehicles[0][0])
# A) trek
# B) audi
# C) redline
# D) specialized

# 2
bicycles = ["trek", "cannondale", "redline", "specialized"]

cars = ["audi", "bmw", "subaru", "toyota"]

vehicles = [bicycles, cars]

for vehicle in vehicles:

    print(vehicle)


# A) ['trek', 'cannondale', 'redline', 'specialized']
#    ['audi', 'bmw', 'subaru', 'toyota']
# B) trek
#    audi

# C) trek

#    audi


# D) ['trek', 'cannondale', 'redline', 'specialized']
#    ['audi', 'bmw', 'subaru', 'toyota']
#    trek
#    audi


# 3
bicycles = ["trek", "cannondale", "redline", "specialized"]

cars = ["audi", "bmw", "subaru", "toyota"]

vehicles = [bicycles, cars]

for vehicle in vehicles:

    for item in vehicle:

        print(item)


# Nested functions


def process_user_data(user):
    def hide_sensitive_info(info):
        # Hiding the sensitive part of the info
        return f"{info[:2]}***"

    username = hide_sensitive_info(user["username"])
    email = hide_sensitive_info(user["email"])

    return f"Processed User: {username}, Email: {email}"


# Example user data
user = {"username": "something", "email": "me@gmail.com"}

# Calling the outer function
print(process_user_data(user))
