import numpy as np
import matplotlib.pyplot as plt

# Load all fitness values: shape is (num_generations, population_size)
full_f = np.load('results/Ant_custom/single/full_f.npy')

# Calculate mean and best fitness per generation
mean_fit = np.mean(full_f, axis=1)
best_fit = np.max(full_f, axis=1)



plt.figure(figsize=(8, 5))
plt.scatter(range(len(mean_fit)), mean_fit, label='Mean Fitness')
plt.scatter(range(len(best_fit)), best_fit, label='Best Fitness')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Fitness Curve')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()