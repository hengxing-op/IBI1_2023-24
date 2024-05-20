import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Change the working directory to where the CSV file is stored
os.chdir(r"C:\Users\Star\Desktop\IBIpractice\IBI1_2023-24\Practical_7")

# Import the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show the fourth column (the DALYs) from every 10th row, starting from the first row, for the first 100 rows (inclusive)
print(dalys_data.iloc[0:101:10, 3])

# Retrieve and show DALYs for all rows corresponding to Afghanistan
afghanistan_data = dalys_data.loc[dalys_data['Entity'] == 'Afghanistan', 'DALYs']
print(afghanistan_data)

# Compute the mean DALYs in China
china_data = dalys_data.loc[dalys_data['Entity'] == 'China', ['Year', 'DALYs']]
mean_dalys_china = np.mean(china_data['DALYs'])
dalys_2019_china = china_data.loc[china_data['Year'] == 2019, 'DALYs'].values[0]
print(f"Mean DALYs in China: {mean_dalys_china}")
print(f"DALYs in China in 2019: {dalys_2019_china}")
print("2019 DALYs in China was above the mean." if dalys_2019_china > mean_dalys_china else "2019 DALYs in China was below the mean.")

# Plot the DALYs over time in China
plt.plot(china_data['Year'], china_data['DALYs'], 'b+')
plt.xticks(china_data['Year'], rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Over Time in China')
plt.show()

# Example question: Are there places in the World where the DALYs in 2019 is less than 18,000? If so, where are they?
low_dalys_2019 = dalys_data[(dalys_data['Year'] == 2019) & (dalys_data['DALYs'] < 18000)]
print(low_dalys_2019)