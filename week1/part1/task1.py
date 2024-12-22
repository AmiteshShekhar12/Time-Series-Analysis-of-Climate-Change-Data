import numpy as np
import matplotlib.pyplot as plt

#number of samples
num_samples = 10000

# Generate samples for each distribution
beta_samples = np.random.beta(a=4, b=20, size=num_samples) * 100
exponential_samples = np.random.exponential(scale=0.1, size=num_samples) * 100
gamma_samples = np.random.gamma(shape=2, scale=0.1, size=num_samples) * 100
laplace_samples = np.random.laplace(loc=0, scale=0.5, size=num_samples) * 100
normal_samples = np.random.normal(loc=0, scale=3, size=num_samples)
poisson_samples = np.random.poisson(lam=3, size=num_samples)

# Create a figure with 6 subplots (3x2 layout)
fig, axs = plt.subplots(3, 2, figsize=(14, 20))

# Plot the histograms
axs[0, 0].hist(beta_samples, bins=range(-5, 51), edgecolor='black')
axs[0, 0].set_title('Beta Distribution')
axs[0, 0].set_xlim([-5, 50])

axs[0, 1].hist(exponential_samples, bins=range(-1, 51), edgecolor='black')
axs[0, 1].set_title('Exponential Distribution')
axs[0, 1].set_xlim([-1, 50])

axs[1, 0].hist(gamma_samples, bins=range(-1, 51), edgecolor='black')
axs[1, 0].set_title('Gamma Distribution')
axs[1, 0].set_xlim([-1, 50])

axs[1, 1].hist(laplace_samples, bins=range(-1, 51), edgecolor='black')
axs[1, 1].set_title('Laplace Distribution')
axs[1, 1].set_xlim([-1, 50])

axs[2, 0].hist(normal_samples, bins=range(-10, 12), edgecolor='black')
axs[2, 0].set_title('Normal Distribution')
axs[2, 0].set_xlim([-10, 11])

axs[2, 1].hist(poisson_samples, bins=range(-1, 12), edgecolor='black')
axs[2, 1].set_title('Poisson Distribution')
axs[2, 1].set_xlim([-1, 11])

# show plot
plt.tight_layout()
plt.show()

# Save the plot
fig.savefig('distributions_plot.png')