#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import math
import matplotlib.pyplot as plt


# In[130]:


#1(a) Inverse method
U = np.random.uniform(0, 1)
X = math.sqrt(2*U+1/4)-1/2
X


# In[131]:


#1(b) AR_Method
U = np.random.uniform(0, 1, 2)
Y = U[0]                        #inverse func. of fY(y)
while(U[1] > (1+2*Y)/3):
    U = np.random.uniform(0, 1, 2)
    Y = U[0]
X = Y
X


# In[132]:


#1(c) composition method
U = np.random.uniform(0, 1, 2)
if U[1] <= 1/2:
    X = U[0]
else:
    X = math.sqrt(U[0])
X


# In[133]:


#2-1 AR_Method
U = np.random.uniform(0, 1, 2)
Y = -math.log(U[0])
while(U[1] > 3*(1+2*math.exp(-Y)-3*math.exp((-2)*Y))/4):
    U = np.random.uniform(0, 1, 2)
    Y = -math.log(U[0])
X = Y
X


# In[134]:


#2-2
U = np.random.uniform(0, 1, 2)
Y = -math.log(U[0])
Z = -math.log(U[1])/2
X = max(Y,Z)
X


# In[136]:


#3-1 AR_Method
U = np.random.uniform(0, 1, 2)
Y = U[0]
while(U[1] > (1/4+2*pow(Y,3)+5*pow(Y,4)/4)/3.5 ):
    U = np.random.uniform(0, 1, 2)
    Y = U[0]
X = Y
X


# In[137]:


#3-2 composition method
U = np.random.uniform(0, 1, 2)
if U[1] <= 1/2 :
    X = pow(U[0],1/4)
elif U[1] <= 3/4 :
    X = pow(U[0],1/5)
else: 
    X = U[0]
X


# In[ ]:




