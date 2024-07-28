# print the middle value from the list


# if the name has even number of characters, print the two middle characters

# if the name has odd number of characters, print the middle character

# if the name has only one character, print the character

# solution
list1 = ["shaukat", "shakir"]
for name in list1:
    if len(name) % 2 == 0:
        index = len(name) // 2
        secondValue = name[index]
        firstValue = name[index - 1]
    else:
        index = len(name) // 2
        print(name[index])


# factorial using while loop in python

num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1

print(factorial)

# simple approach
num = 5

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(factorial)


# another question
import pandas as pd

# Example data
data = {
    "Continent": [
        "Asia",
        "Africa",
        "North America",
        "South America",
        "Antarctica",
        "Europe",
        "Australia",
        "Asia",
        "Africa",
        "Europe",
    ],
    "Country": [
        "China",
        "Nigeria",
        "USA",
        "Brazil",
        "Antarctica",
        "Germany",
        "Australia",
        "India",
        "Egypt",
        "France",
    ],
    "Area": [
        9596960,
        923768,
        9833517,
        8515767,
        14000000,
        357022,
        7692024,
        3287263,
        1002450,
        551695,
    ],
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Grouping by 'Continent' and calculating the mean area
mean_area_by_continent = df.groupby("Continent")["Area"].mean()

# Display the result
print("\nMean Area by Continent:")
print(mean_area_by_continent)
