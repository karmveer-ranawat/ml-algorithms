import numpy as np
math = [84, 82, 81, 89, 73, 94, 92, 70, 88, 95]
science = [85, 82, 72, 77, 75, 89, 95, 84, 77, 94]
history = [97, 94, 93, 95, 88, 82, 78, 84, 69, 78]
data = np.array([math, science, history])

np.cov(data, bias=True)
np.array([[ 64.96, 33.2 , -24.44], [ 33.2 , 56.4 , -24.1 ], [-24.44, -24.1 , 75.]])
import seaborn as sns
import matplotlib.pyplot as plt
cov = np.cov(data, bias=True)
labs = ['math', 'science', 'history']
sns.heatmap(cov, annot=True, fmt='g', xticklabels=labs, yticklabels=labs)
plt.show()
sns.heatmap(cov, annot=True, fmt='g', xticklabels=labs, yticklabels=labs, cmap='coolwarm')
plt.show()
