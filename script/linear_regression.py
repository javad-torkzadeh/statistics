'''
compute weights(betas) for each independent variable
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
####################### open file
'''dataframe = pd.read_csv("../data/age_pressure.csv", delimiter=' ')
X = np.array(dataframe['age'])
Y = np.array(dataframe['blood_pressure'])
print(X)
print(Y)
print(X.shape)
print(Y.shape)

########################### preprocess X & Y
Y = Y.reshape(-1,1)
print(Y)
print(Y.shape)
print(dataframe.shape)
X = X.reshape(-1,1)
print(X.shape)
column1 = np.ones((X.shape[0],1))
print("kgc" , column1)
print(np.concatenate((column1 , X), axis = 1))
X = np.concatenate((column1,X), axis = 1)

#################################### compute beta
print(X.T)
beta = np.dot( (np.linalg.inv(np.dot((X.T) , X))) , (np.dot((X.T) , Y)))
print(beta)
print(beta.T.shape)
print(beta.T)
print("Beta0 is: " ,beta[0,0] , "\n beta1 is :" , beta[1,0] )

################################## plotting
fx = [ beta[0,0] + beta[1,0] * age for age in dataframe['age']]
print(fx)
plt.scatter(dataframe['age'],dataframe['blood_pressure'] , color = 'red' , marker = '+')
plt.plot( dataframe['age'] , fx )

plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.title('Blood Pressure vs. Age')
plt.show()'''
###################################################### brain_weight linier_regression
dataframe = pd.read_csv("../data/brain_weight.csv", delimiter=',')
Xg = np.array(dataframe['gender'])
Xage = np.array(dataframe['age_range'])
Xhv = np.array(dataframe['head_volumn'])
Y = np.array(dataframe['brain_weight'])
print(Xage)
######################################## processing
Y = Y.reshape(-1,1)
print(Y)
print(Y.shape)
print(dataframe.shape)
Xg = Xg.reshape(-1,1)
Xage = Xage.reshape(-1,1)
Xhv = Xhv.reshape(-1,1)
print(Xg.shape)
column1 = np.ones((Xg.shape[0],1))
print("kgc" , column1)
print(np.concatenate((column1 , Xg), axis = 1))
Xg = np.concatenate((column1,Xg), axis = 1)
X = np.concatenate((Xg,Xage,Xhv) , axis=1)
print(X)
beta = np.dot( (np.linalg.inv(np.dot((X.T) , X))) , (np.dot((X.T) , Y)))
print(beta)
###################################