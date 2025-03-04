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



##2nd uni and multi





import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample dataset for demonstration
np.random.seed(42)
data = pd.DataFrame({
    'Feature1': np.random.normal(loc=0, scale=1, size=100),
    'Feature2': np.random.normal(loc=5, scale=2, size=100),
    'Feature3': np.random.normal(loc=3, scale=1, size=100),
    'Category': np.random.choice(['A', 'B', 'C'], size=100)  # Categorical variable
})

# Univariate Distribution Analysis
sns.set(style="whitegrid")

# Plotting Univariate Distribution with different color palettes
plt.figure(figsize=(12, 6))
sns.histplot(data['Feature1'], kde=True, color="blue", bins=20, palette="coolwarm")
plt.title('Univariate Distribution: Feature1')
plt.show()

# Univariate KDE plot with a different color palette
plt.figure(figsize=(12, 6))
sns.kdeplot(data['Feature2'], color="green", shade=True, palette="magma")
plt.title('Univariate Distribution: Feature2')
plt.show()

# Multivariate Distribution Analysis (Pairplot with color by category)
plt.figure(figsize=(12, 8))
sns.pairplot(data, hue="Category", palette="Set2")
plt.suptitle("Multivariate Distribution: Pairplot with Color Palettes", y=1.02)
plt.show()

# Scatter plot for Feature1 vs Feature2, color by Category
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Feature1', y='Feature2', hue='Category', data=data, palette="viridis")
plt.title('Scatterplot of Feature1 vs Feature2 (Color-coded by Category)')
plt.show()


