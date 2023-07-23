import numpy as np
from matplotlib import pyplot as plt 
from numpy import linspace
import random


X = linspace(-10,7,100)
#Y = 0.1*X**4 -4*X**2 - X # wise operations
Y = X**4 + 7*X**3 + 5*X**2 - 17
np.random.seed(5)
x_i = np.random.normal(0,1)
print(x_i)
plt.plot(X,Y,'b-',x_i, 0.1*x_i**4 -4*x_i**2 - x_i, 'ro')

# Gradient Descent Method
alpha = 0.1
grad = 10
print("x_initial = %.4f " % x_i )
grad_vector = []
iter_vector = []
#for i in range(n_ite):
i=1
while np.abs(grad) > 0.00000000001:
  print("\n Iteration number = ",i)
  #grad = 0.4*x_i**3 -8*x_i - 1
  grad = 4*x_i**3 - 21*x_i**2 + 10*x_i#derivada
  grad_vector.append(grad)
  iter_vector.append(i)
  x_i = x_i - alpha*grad
  print("(x_i = %.2f " % x_i, " grad= %.6f " % grad)
  i +=1 
plt.plot(X,Y,'b-',x_i,0.1*x_i**4 -4*x_i**2 - x_i, 'ro')
