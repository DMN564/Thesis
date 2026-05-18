import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('final_events.txt')

q2_vals   = data[:, 1]
eps_vals = data[:, 3]

m, b = np.polyfit(q2_vals, eps_vals, 1)
x_fit = np.linspace(min(q2_vals), max(q2_vals), 1000)
y_fit = m * x_fit + b

plt.figure(figsize=(6,6))
plt.scatter(q2_vals, eps_vals, alpha=0.3, s=50)
plt.plot(x_fit, y_fit, linewidth=2)

plt.xlabel(r"$q_2$",fontsize=18)
plt.grid(True)
plt.tight_layout()
plt.ylabel(r"$\varepsilon_2$",fontsize=18)
plt.title(r"$\epsilon_2$ vs $q_2$",fontsize=18)
plt.savefig("q2_vs_epsilon2_fit.png", dpi=300)
plt.show()
