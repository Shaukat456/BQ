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
    factorial = factorial * num
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


# A 2-D Heatmap is a data visualization tool that helps to represent the magnitude of the matrix in form of a colored table. In Python, we can plot 2-D Heatmaps using the Matplotlib and Seaborn packages. There are different methods to plot 2-D Heatmaps, some of which are discussed below.

# Use Cases For Heatmaps
# As we know the Heatmap is just a colored representation of a matrix. However, heatmap has a very large use case. We can use heatmaps for the following purpose.

#  It is used to see the correlation between columns of a dataset where we can use a darker color for columns having a high correlation.
#  We can also use heatmaps for plotting various time series and finance-related data where the Y-axis will be the month and X-axis will be the year and the element of the heatmap will be our data.


# Create a 12×12 Heatmap with Random data using Matplotlib
# Program to plot 2-D Heat map
# using matplotlib.pyplot.imshow() method
import numpy as np
import matplotlib.pyplot as plt

data = np.random.random((12, 12))
plt.imshow(data)

plt.title("2-D Heat Map")
plt.show()


# Choosing Different Colormaps in Heatmap Using Matplotlib

# Program to plot 2-D Heat map
# using matplotlib.pyplot.imshow() method
import numpy as np
import matplotlib.pyplot as plt

data = np.random.random((12, 12))
plt.imshow(data, cmap="autumn")

plt.title("Heatmap with different color")
plt.show()


# The imshow function in matplotlib.pyplot is used to display data as an image, i.e., on a 2D regular raster. It is particularly useful for visualizing matrices or 2D arrays.

# interpolation Parameter
# The interpolation parameter in the imshow function determines how the image is resampled. This is important when the displayed image has a different resolution than the data. Different interpolation methods can affect the appearance of the image, especially when zooming in or out.


data = np.random.random((12, 12))
plt.imshow(data, cmap="autumn", interpolation="nearest")

# Add colorbar
plt.colorbar()

plt.title("Heatmap with color bar")
plt.show()
