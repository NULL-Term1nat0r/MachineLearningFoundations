import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

plt.scatter(data.experience, data.wage)
plt.show()

def loss_function(m, b, points):
    total_error = 0
    for i = in range(len(points)):
        x = points.iloc[i].experience
        y = points.iloc[i].wage
        total_error += (y - (m * x + b)) ** 2
   total_error / float(len(points))     

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
