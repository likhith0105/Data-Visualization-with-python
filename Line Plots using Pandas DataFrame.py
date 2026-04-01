import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
df2 = pd.DataFrame({
    'a': np.random.normal(loc=0, scale=1, size=1000), 
    'b': np.random.uniform(low=-3, high=3, size=1000)
})

df2.plot()


plt.title("KDE Plot of Column 'a'")
plt.xlabel("Value")
plt.ylabel("Density")

plt.show()
