from matplotlib import pyplot as plt
from random import * 

years = range(2010, 2020)
gdp = [ year * random() for year in years]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.show()