import numpy as np
m = np.array([[1,2,3],[4,5,6]])
print(m)
print(m.shape)
print(m.T)
print(m.T.shape)
print(m.reshape(3,2))
#**********************
print(np.zeros(30))
m = np.ones(30)
print(np.ones(30))
column_1 = m.reshape(-1,1)
print(column_1)
#**********************
column_one = np.ones(30).reshape(-1,1)
print(column_one)
#**********************
column_on = np.ones((30,1))
print(column_on)