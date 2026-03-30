import matplotlib.pyplot as plt
import pandas as pd

cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 13, 35, 15, 12]
explode = [0.1, 0.5, 0, 0, 0]
colors = ( "orange", "cyan", "yellow","grey", "green",)

plt.pie(data, labels=cars, explode=explode, autopct='%1.2f%%',colors=colors, shadow=True)
plt.show()