#!/usr/bin/env python
# coding: utf-8

# In[13]:


def DFS(v):
    if v== n+1:
        for i in range(1,n+1):
            if ch[i] ==1:
                print(i, end ='')
    else:
        ch[v]=1
        DFS(n+1)
        ch[v]=0
        DFS(n+1)

n= int(input())
ch=[0]*(n+1)
DFS(1)    


# In[ ]:




