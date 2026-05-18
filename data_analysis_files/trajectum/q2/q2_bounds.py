import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    pass

data = np.loadtxt("txt_files/final_events.txt")

q2_values = data[:, 1]
print(q2_values)
q2_20 = np.percentile(q2_values, 20)
q2_80 = np.percentile(q2_values, 80)

print(f"20th percentile q2 value: {q2_20:.6f}")
print(f"80th percentile q2 value: {q2_80:.6f}")

plt.figure(figsize=(8, 6))

plt.hist(q2_values, bins=40, alpha=0.6, label="q2 distribution")

plt.axvspan(q2_values.min(), q2_20, alpha=0.3, label=f"Bottom 20% (q2 < {q2_20:.3f})")

plt.axvspan(q2_80, q2_values.max(), alpha=0.3, label=f"Top 20% (q2 > {q2_80:.3f})")

plt.axvline(q2_20, linestyle="--", linewidth=2, label="20th percentile")
plt.axvline(q2_80, linestyle="--", linewidth=2, label="80th percentile")

plt.xlabel(r"$q_2$")
plt.ylabel("Counts")
plt.title(r"$q_2$ Distribution with Event Shape Percentiles")
plt.legend()

plt.tight_layout()

plt.show()
