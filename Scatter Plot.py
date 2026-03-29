import pandas as pd
import matplotlib.pyplot as plt
import os
import requests # Import requests library



# Check if 'tips.csv' exists, if not, download it
file_path = "tips.csv"
if not os.path.exists(file_path):
    print(f"{file_path} not found. Downloading it...")
    # URL for the tips dataset, common source is seaborn or github gists
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"{file_path} downloaded successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {file_path}: {e}")
        # Optionally, raise the error or handle it differently if download fails
        raise

# reading the database
data = pd.read_csv(file_path)

# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()