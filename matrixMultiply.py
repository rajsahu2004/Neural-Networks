import numpy as np
a = np.array([[1.,-1.,0.1],[2,-2.,0.2]])
w = np.array([[3,5,7,9],[4,6,8,0]])
at = a.T
z = np.matmul(at,w)
print(z)
AT = np.array([[200,17]])
W = np.array([[1,-3,5],[-2,4,-6]])
B = np.array([[-1,1,2]])
Z = np.matmul(AT,W)+B
print(Z)