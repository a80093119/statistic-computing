#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np
import math
from scipy import stats
from scipy.stats import binom, norm, beta, expon


# In[7]:


E = []
for j in range(10):
    XYZ = []
    for i in range(1000):
        y = 0.5
        z = 0.5
        for k in range(1000):
            U = np.random.uniform(0, 1, 3)
            x = -math.log(U[0])/(y+z+1)
            y = -math.log(U[1])/(x+z+1)
            z = -math.log(U[2])/(x+y+1)
        XYZ.append(x*y*z)
    E.append(sum(XYZ)/1000)
print("E(XYZ) = ", sum(E)/10)


# In[64]:


X = []
Y = []
N = []
for i in range(1000):
    n = 5
    y = 0.5
    for j in range(1000):
        x = binom.rvs(n, y)
        y = beta.rvs(x+2, n-x+3)
        nhat = np.random.poisson(lam = 4*(1-y))
        n = nhat+x
    X.append(x)
    Y.append(y)
    N.append(n)
print("E(X) = ", sum(X)/1000)
print("E(Y) = ", sum(Y)/1000)
print("E(N) = ", sum(N)/1000)


# In[ ]:




