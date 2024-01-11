#!/usr/bin/env python
# coding: utf-8

# In[214]:


#1.
import numpy as np
import math


Total = []
n = 1000
for i in range(n):
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    g = math.exp(-(y+1)*(1/x-1))*(1/x-1) / pow(x,2)
    Total.append(g)
print("第一題 = ", sum(Total)/n)


# In[22]:


#2.
import numpy as np
import math

X = []
sim = 1000
for k in range(sim):
    cards = []
    N = 0
    n = 100
    
    cards.append(math.ceil(np.random.uniform(0, 1)*n))
    while(len(cards) < n):
        U = math.ceil(np.random.uniform(0, 1)*n)
        if U in cards:
               continue
        else: 
            cards.append(U)
    for i in range(len(cards)):
        if cards[i] == i+1:
            N = N + 1
    X.append(N)

print("E(N) = ", sum(X)/sim)
print("Var(N) = ", sum(np.power(X,2))/sim - np.power(sum(X)/sim,2))


# In[276]:


#2.Exactly value
import numpy as np
N = []
N_2 = []
n = 100
N.append(1/np.math.factorial(n-1))
N_2.append(pow(n,2)*(1/np.math.factorial(n)))
for i in range(n-1):
    k = []
    for j in range(i+1):
        fac = pow(-1,j+1)*(1/np.math.factorial(j+1))
        k.append(fac)
    X = (99-i)*(1/np.math.factorial(99-i))*(1+sum(k))
    N.append(X)
    X_2 = pow((99-i),2)*(1/np.math.factorial(99-i))*(1+sum(k))
    N_2.append(X_2)
print("Exactly E(N)", sum(N))
print("Exactly Var(N)",sum(N_2) - np.power(sum(N),2))


# In[245]:


#3(a)
import numpy as np
import math

total_X = []
sim = 1000
r = 4
p = 0.5
for i in range(sim):
    X = 0
    count = 0
    while(count < r):
        U = np.random.uniform(0, 1)
        X = X + int(math.log10(U)/math.log10(1-p)) + 1
        count = count + 1
    total_X.append(X)
#total_X
print("E(X) = ", sum(total_X)/sim)


# In[77]:


#3(c)
import numpy as np

r = 4
p = 0.5
total_X = []
sim = 1000
for i in range(sim):
    U = np.random.uniform(0, 1)
    j = r
    X = 0
    P = []
    P.append(np.math.factorial(j-1)/(np.math.factorial(j-r)*np.math.factorial(r-1))*pow(p,r)*pow(1-p,j-r))
    while(U >= sum(P)):
        P.append(j*(1-p)/(j+1-r)*P[j-r])
        if U < sum(P):
            X = j + 1
            break
        else:
            j = j + 1 

    else:
        X = j
    total_X.append(X)
total_X
print("E(X) = ", sum(total_X)/sim)


# In[246]:


#3(d)
import numpy as np
import math

total_X = []
sim = 1000
r = 4
p = 0.5
for i in range(sim):
    X = 0
    count = 0
    while(count < r):
        U = np.random.uniform(0, 1)
        n = 1
        while(U >= p):
            U = np.random.uniform(0, 1)
            n = n + 1
        X = X + n
        count = count + 1
    total_X.append(X)
#total_X
print("E(X) = ", sum(total_X)/sim)

