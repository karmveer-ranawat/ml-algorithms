import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import multivariate_normal, uniform, expon

# Set random seed for reproducibility
np.random.seed(42)

# Create a function to generate and plot bivariate distributions
def plot_bivariate_distribution(dist_type):
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    if dist_type == 'normal':
        # Generate a bivariate normal distribution
        mean = [0, 0]  # Mean of the distribution
        cov = [[1, 0.8], [0.8, 1]]  # Covariance matrix
        data = np.random.multivariate_normal(mean, cov, 500)
        ax.scatter(data[:, 0], data[:, 1], color='b', alpha=0.5)
        ax.set_title("Bivariate Normal Distribution")
    
    elif dist_type == 'uniform':
        # Generate a bivariate uniform distribution
        data = np.random.uniform(low=-5, high=5, size=(500, 2))
        ax.scatter(data[:, 0], data[:, 1], color='g', alpha=0.5)
        ax.set_title("Bivariate Uniform Distribution")
    
    elif dist_type == 'exponential':
        # Generate a bivariate exponential distribution
        data = np.random.exponential(scale=1, size=(500, 2))
        ax.scatter(data[:, 0], data[:, 1], color='r', alpha=0.5)
        ax.set_title("Bivariate Exponential Distribution")
    
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    plt.grid(True)
    plt.show()

# Explore different bivariate distributions
distributions = ['normal', 'uniform', 'exponential']

for dist in distributions:
    plot_bivariate_distribution(dist)
