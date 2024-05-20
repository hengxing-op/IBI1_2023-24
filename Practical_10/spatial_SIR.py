import numpy as np
import matplotlib.pyplot as plt

# Define basic variables
N = 10000  
beta = 0.3  
gamma = 0.05 
grid_size = 100
population = np.zeros((grid_size, grid_size))

# Randomly choose an initial infected person
outbreak = np.random.choice(range(grid_size), 2)
population[outbreak[0], outbreak[1]] = 1

# Define the time steps to save the plots
save_steps = [0, 10, 50, 100]

# Function to update the population grid
def update_population(population):
    new_population = population.copy()
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNeighbour in range(x - 1, x + 2):
            for yNeighbour in range(y - 1, y + 2):
                if (xNeighbour, yNeighbour) != (x, y):
                    if 0 <= xNeighbour < grid_size and 0 <= yNeighbour < grid_size:
                        if population[xNeighbour, yNeighbour] == 0:
                            new_population[xNeighbour, yNeighbour] = np.random.choice([0, 1], p=[1 - beta, beta])
    recover = np.random.choice([0, 2], size=(grid_size, grid_size), p=[1 - gamma, gamma])
    new_population = np.where((population == 1) & (recover == 2), 2, new_population)
    return new_population

# Run the spatial SIR model over 100 time steps
for t in range(101):
    if t in save_steps:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time step {t}')
        plt.show()  
    population = update_population(population)