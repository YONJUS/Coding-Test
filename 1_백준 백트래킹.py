#!/usr/bin/env python
# coding: utf-8

# In[33]:


N,M = map(int,input().split())
visited = [False]* (N+1) #[fa;se, fa;se ... ]
result = [] 


def DFS(num):
    if num == 0:
        print(" ".join(map(str, result)))
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            DFS(num - 1)
            visited[i] = False
            result.pop()

DFS(M)
    


# In[ ]:





# In[ ]:




