import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create a sample DataFrame with some random data
# (creating two columns, 'a' and 'b', though we only plot 'a')
np.random.seed(42)
df2 = pd.DataFrame({
    'a': np.random.normal(loc=0, scale=1, size=1000), # Normal distribution
    'b': np.random.uniform(low=-3, high=3, size=1000)
})

# 2. Generate the KDE plot for column 'a'
df2['a'].plot.kde()

# 3. Add titles and labels (optional but recommended)
plt.title("KDE Plot of Column 'a'")
plt.xlabel("Value")
plt.ylabel("Density")

# 4. Display the plot
plt.show()
