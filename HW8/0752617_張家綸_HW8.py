#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
import math
import pandas as pd
from collections import Counter


# In[52]:


def func1(x):
    Y = []
    U = np.random.uniform(0, 1, x)
    for i in range(x):
        if U[i]<1/6:
            Y.append(1)
        elif U[i]<2/6:
            Y.append(2)
        elif U[i]<3/6:
            Y.append(3)
        elif U[i]<4/6:
            Y.append(4)
        elif U[i]<5/6:
            Y.append(5)
        else:
            Y.append(6)
    return Y
T = 0
sim = 10000
for j in range(sim):
    count = Counter(func1(1000))
    y = []
    for i in range(6):
        y.append(count[i+1])
    y_hat = [pow((N - 1000/6), 2)/(1000/6) for N in y]
    if sum(y_hat)>=2.179:
        T = T+1
print("p-value = ", T/sim)


# In[96]:


count = 0
sim = 10000
for i in range(sim):
    U = pd.Series(np.ceil(100*np.random.uniform(0, 1, 21)))
    R = U.rank()
    R_hat = 12*(pow(sum(R[0:7])-77, 2)+pow(sum(R[7:14])-77, 2)+pow(sum(R[14:21])-77, 2))/(21*22*7)
    if R_hat>=2.5213:
        count = count+1
print("p-value = ", count/sim)

