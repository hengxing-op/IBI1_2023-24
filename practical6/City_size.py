import matplotlib.pyplot as plt

# give the city and corresponding population
uk_data = [('Edinburgh', 0.56), ('Glasgow', 0.62), ('Stirling', 0.04), ('London', 9.7)]
china_data = [('Haining', 0.58), ('Hangzhou', 8.4), ('Shanghai', 29.9), ('Beijing', 22.2)]

# sort the data with population
uk_data_sorted = sorted(uk_data, key=lambda x: x[1])
china_data_sorted = sorted(china_data, key=lambda x: x[1])

# divide the (city,population) into different parts
uk_cities_sorted, uk_populations_sorted = zip(*uk_data_sorted)
china_cities_sorted, china_populations_sorted = zip(*china_data_sorted)

# generate UK bar graph
plt.figure()
plt.bar(uk_cities_sorted, uk_populations_sorted)
plt.title('Population Distribution in UK Cities (2024)')
plt.xlabel('City')
plt.ylabel('Population (millions)')
plt.show()

# generate China bar graph
plt.figure()
plt.bar(china_cities_sorted, china_populations_sorted)
plt.title('Population Distribution in China Cities (2024)')
plt.xlabel('City')
plt.ylabel('Population (millions)')
plt.show()