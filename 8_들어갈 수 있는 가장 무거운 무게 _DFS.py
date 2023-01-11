#!/usr/bin/env python
# coding: utf-8

# # Q) C킬로그램이 넘지 않게 태워야 되는 조건 
# - 1) N마리의 바둑이 2) 각 마둑이의 무게 W1,... ,Wn 3) C킬로 미만이면서 4) 그 값이 최대일 것 
# 

# # A)
# - 각 부분 집합을 구함 
# - result값과 sum값을 비교한 뒤, sum값이 result보다 크면 result에 업데이트시킨다

# In[6]:


def DFS(L, sum): #L = index , sum
    global result
    
    if L == n: # 부분집합 하나가 완성됨
        if sum> c: # sum이 c보다 작은거만 나오게함 
            return
        if sum>result:
            result = sum
    else:
        DFS(L+1, sum+a[L]) # a[L]을 부분 집합에 넣음 
        DFS(L+1, sum) # a[L]을 부분집합으로 참여 x 
        
    
        
            


# In[7]:


c,n = map(int, input().split())
a = [0]* n 
result = -2147000000 #가장 큰 값 넣기 & 초기값은 가장 낮ㅇ느 값 
for i in range(n):
    a[i]=int(input())
DFS(0,0)
print(result)


# In[ ]:





# In[ ]:





# In[ ]:




