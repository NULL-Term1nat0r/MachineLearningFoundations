import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

plt.scatter(data.experience, data.wage)
plt.show()