#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

U = np.random.uniform(0, 1, 100)
print("11(a) = ", np.corrcoef(U, np.sqrt(1-pow(U,2)))[0,1]) 
print("11(b) = ", np.corrcoef(pow(U,2), np.sqrt(1-pow(U,2)))[0,1]) 


# In[8]:


import numpy as np

num = [100, 1000, 1000]
value = []
for k in num:
    N = []
    n = k
    for i in range(n):
        count = 1
        U = np.random.uniform(0, 1)
        for j in range(10000):
            if U < 1:
                U = U + np.random.uniform(0, 1)
                count = count + 1
            else: 
                N.append(count)
                count = 0
                break
    value.append(sum(N)/n)
value

