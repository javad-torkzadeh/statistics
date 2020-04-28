'''
1: read csv file using pandas
2: compute average & variance & std of each column using numpy
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataframe = pd.read_csv("../data/age_pressure.csv", delimiter=' ')
print(list(dataframe.columns))
print(dataframe['age'])
print(dataframe['blood_pressure'])

print(f'Average of age is: {np.mean(dataframe["age"])}')
print(f'Variance of age is: {np.var(dataframe["age"])}')
print(f'Standard deviation of age is: {np.std(dataframe["age"])}')

print(f'Average of blood pressure is: {np.mean(dataframe["blood_pressure"])}')
print(f'Variance of blood pressure is: {np.var(dataframe["blood_pressure"])}')
print(f'Standard deviation of blood pressure is: {np.std(dataframe["blood_pressure"])}')

plt.scatter(dataframe['age'],dataframe['blood_pressure'] , color = 'red' , marker = '+')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.title('Blood Pressure vs. Age')
plt.show()

