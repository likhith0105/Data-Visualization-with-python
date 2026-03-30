import matplotlib.pyplot as plt

year = ['2010', '2002', '2004', '2006', '2008']
production = [25, 15, 35, 30, 10]

plt.bar(year, production)

plt.savefig("output.jpg")
plt.savefig("output1", facecolor='y', bbox_inches="tight",pad_inches=0.3, transparent=True)