import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

df = pd.DataFrame(data)
print(df)


# Subsetting in Pandas
# Subsetting involves selecting rows, columns, or both from a DataFrame. Here are some common ways to subset data in pandas

# Selecting a single column
print(df["Name"])


# Selecting multiple columns
print(df[["Name", "City"]])


# Selecting rows by index
print(df.loc[0])


# Selecting rows by condition
print(df[df["Age"] > 25 or df["City"] == "New York"])


# Selecting rows and columns
# explain the below code


print(df.loc[1, "Name"])


# Modifying DataFrames
# You can modify the values in a DataFrame in a similar way to modifying values in a list. For example, you can change the value of a specific cell by using the loc[] method to access the row and column you want to modify, and then assigning a new value to that cell. Here’s an example:

df.loc[0, "Age"] = 25

print(df)


# Adding Rows to a DataFrame
# You can add rows to a DataFrame by using the append() method. Here’s an example:

new_row = {"Name": "Eve", "Age": 28, "City": "Miami"}

df = df.append(new_row)

print(df)


# Removing Rows from a DataFrame
# You can remove rows from a DataFrame by using the drop() method. Here’s an example

df = df.drop(0)

print(df)


# Merging DataFrames
# You can merge two DataFrames by using the merge() method. Here’s an example:

data2 = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Salary": [50000, 60000, 70000, 80000],
}

df2 = pd.DataFrame(data2)

df = pd.merge(df, df2)

print(df)


# conditional subsetting

print(df[df["Salary"] > 60000])


# Grouping Data

# You can group data in a DataFrame by using the groupby() method. Here’s an example:

grouped = df.groupby("City")

print(grouped.mean())
