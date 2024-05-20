# Import necessary libraries
import matplotlib.pyplot as plt

# Data for the populations of cities in the UK and China
uk_cities = [0.56, 0.62, 0.04, 9.7]
china_cities = [0.58, 8.4, 29.9, 22.2]

# Sorting the populations of cities
sorted_uk_cities = sorted(uk_cities)
sorted_china_cities = sorted(china_cities)

# Print sorted lists of city sizes
print("Sorted UK city populations:", sorted_uk_cities)
print("Sorted China city populations:", sorted_china_cities)

# Bar plot for UK city populations
plt.figure(figsize=(10, 5))
plt.bar(['Edinburgh', 'Glasgow', 'Stirling', 'London'], uk_cities, color='blue')
plt.title('City Populations in the UK')
plt.xlabel('City')
plt.ylabel('Population (millions)')
plt.show()

# Bar plot for China city populations
plt.figure(figsize=(10, 5))
plt.bar(['Haining', 'Hangzhou', 'Shanghai', 'Beijing'], china_cities, color='red')
plt.title('City Populations in China')
plt.xlabel('City')
plt.ylabel('Population (millions)')
plt.show()