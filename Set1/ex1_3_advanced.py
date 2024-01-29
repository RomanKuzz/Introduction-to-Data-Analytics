import numpy as np

years = np.random.randint(2010, 2021, 10)

prices = np.random.randint(2000, 60000, 10)

# Sort both datasets according to years
sort_arg = np.argsort(years)
years = years[sort_arg]
prices = prices[sort_arg]

# Print the sorted datasets
print("Manufacturing years:")
print(years)
print("Selling prices:")
print(prices)