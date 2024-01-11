#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import math


# In[47]:


sim = 1000
n =0
sd = 1
while(sd >= 0.01):
    EX = []
    n = n+100
    for i in range(sim):
        X = np.random.exponential(scale = 1.0, size = n)
        EX.append(10 + np.mean(X)) 
    sd = np.std(EX)
    
print("E(X|X>10) = ", np.mean(EX))
print("sd(mean(EX)) = ", sd)
print("n = ", n)


# In[36]:


sim = 1000
n =0
sd = 1
while(sd >= 0.01):
    n = n+100
    EX = []
    for i in range(sim):
        X = np.random.exponential(scale = 10, size = n)
        y = [10*math.exp(-0.9*a) for a in X]
        EX.append(10 + np.mean(X * y)) 
    sd = np.std(EX)
    
print("E(X|X>10) = ", np.mean(EX))
print("sd(mean(EX)) = ", sd)
print("n = ", n)


# In[ ]:




