# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the basic variables
N = 10000  
beta = 0.3  
gamma = 0.05  
S = [9999]  
I = [1]  
R = [0]  

# Run the SIR model over 1000 time steps
for t in range(1000):
    # Calculate the probabilities
    p_infected = beta * I[-1] / N
    p_recovered = gamma

    # Determine new infections and recoveries
    new_infected = np.random.choice([0, 1], S[-1], p=[1-p_infected, p_infected]).sum()
    new_recovered = np.random.choice([0, 1], I[-1], p=[1-p_recovered, p_recovered]).sum()

    # Update the counts
    S.append(S[-1] - new_infected)
    I.append(I[-1] + new_infected - new_recovered)
    R.append(R[-1] + new_recovered)

# Plot the results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()
plt.savefig('SIR_plot.png')
plt.show()