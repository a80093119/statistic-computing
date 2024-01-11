#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import math


# In[81]:


n = 1000
sim = 100
average_spendtime = []
theta = []
var = []
for k in range(n):
    t = 0
    I = 0
    T = 5
    S = []
    lam = 4
    D = []
    spend_time = []
    count = 0
    U = np.random.uniform(0,1)
    t = t -math.log(U)/lam
    while(t <= T):
        I = I+1
        S.append(t)
        U = np.random.uniform(0,1)
        t = t -math.log(U)/lam

    U = np.random.uniform(0,1)
    G = -math.log(U)/4.2
    D.append(S[0]+G)
    spend_time.append(D[0]-S[0])
    for i in range(3):
        U = np.random.uniform(0,1)
        G = -math.log(U)/4.2
        D.append(max(D[i], S[i+1])+G)
        spend_time.append(D[i+1]-S[i+1])
    for j in range(4,I):
        if S[j] > D[count]:
            count = count + 1
            U = np.random.uniform(0,1)
            G = -math.log(U)/4.2
            D.append(max(D[count+2], S[j])+G)
            spend_time.append(D[count+3]-S[j])
    average = sum(spend_time)/len(spend_time)
    average_spendtime.append(average)
for i in range(sim):
    X = np.random.choice(average_spendtime, n)
    theta.append(sum(X)/n)
theta_mean = sum(theta)/sim
bias = theta_mean - sum(average_spendtime)/n
for j in range(sim):
    var.append(pow(theta[j]-theta_mean,2))
variance = sum(var)/(sim-1)
print("average spend time = ", sum(average_spendtime)/n)
MSE = pow(bias,2) + variance
print("MSE = ", MSE)


# In[ ]:




