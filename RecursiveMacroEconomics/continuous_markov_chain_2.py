import  numpy  as np
import matplotlib.pyplot as plt

from scipy.stats import norm,gaussian_kde
from quantecon import LAE

n = 20
k = 5000
J = 6
theta = 0.9
d = np.sqrt(1 - theta ** 2)
delta = theta / d

fig, axes = plt.subplots(J, 1, figsize=(10, 4 * J))
initial_condition = np.linspace(8, 0, J)

X = np.empty((k, n))

for j in range(J):
    axes[j].set_ylim(-4, 8)
    title = "time series from t" + str(initial_condition[j])
    axes[j].set_title(title)

    Z = np.random.randn(k, n)

    X[:, 0] = initial_condition[j]
    for t in range(1, n):
        X[:, t] = theta * np.abs(X[:, t - 1]) + d * Z[:, t]
    axes[j].boxplot(X)

plt.show()