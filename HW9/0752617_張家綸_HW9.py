#!/usr/bin/env python
# coding: utf-8

# In[71]:


import numpy as np
import math
import matplotlib.pyplot as plt


# In[72]:


times = []
sim = 1000
n = 9
for k in range(sim):
    T = 0
    X = np.random.uniform(0, 1, n)
    X_sort = sorted(X)
    Z = []
    for j in range(n-1):
        Z.append(X_sort[j+1] - X_sort[j])
    Z = np.array(Z)
    while (Z <= 0.1).any() == True:
        U = np.random.uniform(0, 1)
        index = int(n*U)
        new = np.random.uniform(0, 1)
        Y = np.delete(X, index)
        d = np.array([abs(a - new) for a in Y])
        if (d > 0.1).all() == True:
            X[index] = new
        X_sort = sorted(X)
        Z = []
        for i in range(n-1):
            Z.append(X_sort[i+1] - X_sort[i])
        Z = np.array(Z)
        T = T + 1
    times.append(T)
times
plt.hist(times)
plt.show()


# In[ ]:




