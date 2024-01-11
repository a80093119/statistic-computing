#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import math


# In[227]:


#a
variance = []
mean_spendtime = []
sim = 10000
for j in range(sim):    
    t = 0
    I = 0
    T = 15
    S = []
    lam = 2
    D = []
    spend_time = []
    U = np.random.uniform(0,1)
    t = t -math.log(U)/lam
    while(t <= T):
        I = I+1
        S.append(t)
        U = np.random.uniform(0,1)
        t = t -math.log(U)/lam

    U = np.random.uniform(0,1)
    G = -math.log(U)
    D.append(S[0]+G)
    spend_time.append(D[0] - S[0])
    for i in range(9):
        U = np.random.uniform(0,1)
        G = -math.log(U)
        D.append(max(D[i], S[i+1])+G)
        spend_time.append(D[i+1]-S[i+1])
    theta = sum(spend_time)
    mean_spendtime.append(theta)
print("theta hat", np.mean(mean_spendtime)) 
print("variance", np.var(mean_spendtime))


# In[11]:


#b
variance = []
mean_spendtime = []
sim = 10000
for j in range(sim):    
    t1 = 0
    t2 = 0
    S1 = []
    S2 = []
    lam = 2
    D1 = []
    D2 = []
    spend_time1 = []
    spend_time2 = []
    U = np.random.uniform(0,1,10)
    for w in range(10):
        t1 = t1 -math.log(U[w])/lam
        S1.append(t1)
        t2 = t2 -math.log(1-U[w])/lam
        S2.append(t2)
    U = np.random.uniform(0,1)
    G1 = -math.log(U)
    G2 = -math.log(1-U)
    D1.append(S1[0]+G1)
    spend_time1.append(D1[0] - S1[0])
    D2.append(S2[0]+G2)
    spend_time2.append(D2[0] - S2[0])
    for i in range(9):
        U = np.random.uniform(0,1)
        G1 = -math.log(U)
        G2 = -math.log(1-U)
        D1.append(max(D1[i], S1[i+1]) + G1)
        spend_time1.append(D1[i+1]-S1[i+1])
        D2.append(max(D2[i], S2[i+1]) + G2)
        spend_time2.append(D2[i+1]-S2[i+1])
    theta1 = sum(spend_time1)
    theta2 = sum(spend_time2)
    mean_spendtime.append((theta1+theta2)/2)
print("theta hat", np.mean(mean_spendtime)) 
print("variance", np.var(mean_spendtime))


# In[5]:


#c
Y = []
variance = []
mean_spendtime = []
sim = 10000
for j in range(sim):    
    t = 0
    S = []
    y = []
    lam = 2
    D = []
    spend_time = []
    U = np.random.uniform(0,1,10)
    for w in range(10):
        t = t -math.log(U[w])/lam
        S.append(t)
    U = np.random.uniform(0,1)
    G = -math.log(U)
    y.append(G)
    D.append(S[0]+G)
    spend_time.append(D[0] - S[0])
    for i in range(9):
        U = np.random.uniform(0,1)
        G = -math.log(U)
        y.append(G)
        D.append(max(D[i], S[i+1])+G)
        spend_time.append(D[i+1]-S[i+1])
    theta = sum(spend_time)
    Y.append(10*np.mean(y))
    mean_spendtime.append(theta)
print("theta hat", np.mean(mean_spendtime)) 
print("variance", np.var(mean_spendtime) - pow(np.cov(mean_spendtime,Y)[1][0],2)/np.var(Y))


# In[7]:


#d
Y = []
variance = []
mean_spendtime = []
sim = 10000
for j in range(sim):    
    t = 0
    S = []
    I = []
    y = []
    lam = 2
    D = []
    spend_time = []
    U = np.random.uniform(0,1,10)
    for w in range(10):
        t = t -math.log(U[w])/lam
        S.append(t)
        I.append(-math.log(U[w])/lam)
    del I[9]
    U = np.random.uniform(0,1)
    G = -math.log(U)
    y.append(G)
    D.append(S[0]+G)
    spend_time.append(D[0] - S[0])
    for i in range(9):
        U = np.random.uniform(0,1)
        G = -math.log(U)
        y.append(G)
        D.append(max(D[i], S[i+1])+G)
        spend_time.append(D[i+1]-S[i+1])
    theta = sum(spend_time)
    Y.append(10*np.mean(y) - 9*np.mean(I))
    mean_spendtime.append(theta)
print("theta hat", np.mean(mean_spendtime)) 
print("variance", np.var(mean_spendtime) - pow(np.cov(mean_spendtime,Y)[1][0],2)/np.var(Y))


# In[8]:


#e
variance = []
mean_spendtime = []
sim = 10000
for j in range(sim):    
    t = 0
    S = []
    lam = 2
    D = []
    N = []
    spend_time = []
    U = np.random.uniform(0,1,10)
    for w in range(10):
        t = t -math.log(U[w])/lam
        S.append(t)
    U = np.random.uniform(0,1)
    G = -math.log(U)
    D.append(S[0]+G)
    spend_time.append(D[0] - S[0])
    for i in range(9):
        U = np.random.uniform(0,1)
        G = -math.log(U)
        D.append(max(D[i], S[i+1])+G)
    N.append(0)
    for k in range(9):
        count = 0
        z = 0
        while(z<(k+1)):
            if S[k+1] < D[z]:
                count = count+1
            z = z+1
        N.append(count)
    mean_spendtime.append(sum(N)+10)
print("theta hat", np.mean(mean_spendtime)) 
print("variance", np.var(mean_spendtime))


# In[ ]:




