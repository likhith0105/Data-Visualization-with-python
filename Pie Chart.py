import matplotlib.pyplot as plt
import pandas as pd

cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 10, 35, 15, 12]

plt.pie(data, labels=cars)
plt.title(" Pie Chart")
plt.show()