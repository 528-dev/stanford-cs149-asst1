import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("numthreads_speedup_view2.csv")
plt.title("view2")
plt.xlabel("threads number")
plt.ylabel("speedup")
plt.plot(data["threads"], data["speedup"])

plt.show()