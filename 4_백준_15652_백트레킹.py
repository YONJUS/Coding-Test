#!/usr/bin/env python
# coding: utf-8

# In[32]:


N,M = map(int,input().split())
result = [] 
start = []

def DFS(start):
    if len(result) == M: #리스트의 길이가 m과 같을 때 
        print(" ".join(map(str, result))) #프린트를 해라 
        return
   
    for i in range(start, N+1): # 1부터 n까지 숫자
       
        result.append(i) # i를 집어넣는다 
        DFS(i + 1) #  i+1한 재귀함수를 호출 -> 오름차순으로 들어가기 위함 
        result.pop() # 리스트 pop 

DFS(1)
    


# In[ ]:




