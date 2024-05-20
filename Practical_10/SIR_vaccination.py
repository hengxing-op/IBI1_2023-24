import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define the basic variables
N = 10000  # Total population
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
vaccination_percentages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Vaccination percentages

# Function to simulate the SIR model
def sir_simulation(vaccination_percentage):
    vaccinated = int(N * vaccination_percentage / 100)
    susceptible = N - vaccinated - 1
    S = [susceptible]
    I = [1]
    R = [0]

    # Run the model over 1000 time steps
    for t in range(1000):
        p_infected = beta * I[-1] / N
        p_recovered = gamma

        new_infected = np.random.choice([0, 1], S[-1], p=[1-p_infected, p_infected]).sum() if S[-1] > 0 else 0
        new_recovered = np.random.choice([0, 1], I[-1], p=[1-p_recovered, p_recovered]).sum() if I[-1] > 0 else 0

        S.append(S[-1] - new_infected)
        I.append(I[-1] + new_infected - new_recovered)
        R.append(R[-1] + new_recovered)

    return I

# Plotting the results for different vaccination percentages
plt.figure(figsize=(10, 6), dpi=150)

for vaccination_percentage in vaccination_percentages:
    infected_curve = sir_simulation(vaccination_percentage)
    plt.plot(infected_curve, label=f'{vaccination_percentage}% vaccinated', color=cm.viridis(vaccination_percentage / 100))

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Vaccination')
plt.legend()
plt.savefig('SIR_vaccination_plot.png')
plt.show()