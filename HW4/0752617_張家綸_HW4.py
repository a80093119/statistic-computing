#!/usr/bin/env python
# coding: utf-8

# In[283]:


import numpy as np
import math


# In[284]:


#1.method1
t = 0
I = 0
lam = 7
S = []
T = 10
def lam_t(x):
    return 3+4/(x+1)

U = np.random.uniform(0, 1)
t = t - math.log(U)/lam
while(t <= T):
    U = np.random.uniform(0, 1)
    if U <= lam_t(t)/lam:
        I = I+1
        S.append(t)
    U = np.random.uniform(0, 1)
    t = t - math.log(U)/lam

print("發生事件的時間", S)
print("總次數",I)


# In[285]:


#2.

y = []
y.append([])
y.append([])
y.append([])
for i in range(3):
    for j in range(1000):
        U = np.random.uniform(0, 1, 3)
        Y = -math.log(U[0])
        while(U[1] > math.exp(-pow(Y-1,2)/2)):
            U = np.random.uniform(0, 1, 3)
            Y = -math.log(U[0])
        X = Y
        if U[2] <= 1/2: Z = X
        else: Z = -X
        y[i].append(Z)
        
cor = [[1, 0.5/2, 0.5/3],
        [0.5/2, 1, 0.5/6],
        [0.5/3, 0.5/6, 1]]
L = np.linalg.cholesky(cor)
print(L)
W = np.dot(L, y)
#print(np.mean(W[0]), np.mean(W[0]), np.mean(W[1])) #check mean
#print(np.corrcoef(np.vstack((W[0],W[1],W[2])))) #check correlation
def normal(v):
    dx = 1
    area = 0
    y = 0
    for x in range( 0, 1000, dx):
        x = x/1000
        y = v*math.exp(-pow(v*x, 2)/2)/math.sqrt(2*math.pi)
        area = area + (y * (dx/1000))
    if x>=0: return min(area+0.5, 0.99999999)
    else: return max(area+0.5, 0.00000001)
X = []
X.append([])
X.append([])
X.append([])
for i in range(3):
    for j in range(1000):
        temp = -math.log(1-normal(W[i][j]))*(i+1)
        X[i].append(temp)
Z = np.vstack((X[0],X[1],X[2]))
print("mean = ", np.mean(X[0]), np.mean(X[1]), np.mean(X[2]))
print("var = ", np.var(X[0]), np.var(X[1]), np.var(X[2]))
print("cov = \n", np.cov(Z))
print("cor = \n", np.corrcoef(Z))


# In[ ]:




