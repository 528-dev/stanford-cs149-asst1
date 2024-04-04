import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("vector_utilization.csv")
plt.title("view")
plt.xlabel("vector width")
plt.ylabel("vector utilization")
plt.ylim((0.6, 0.8))
plt.plot(data["width"], data["utilization"], marker="o")

plt.show()