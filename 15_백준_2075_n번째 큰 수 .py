#!/usr/bin/env python
# coding: utf-8

#  # Q) 
#  
#  - N×N의 표에 수 N2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다. N=5일 때의 예를 보자

# # A) 
# 
#  1. n입력 받고 
#  2. 2중 포문으로 n*n번 입력 받은 뒤, 
#  3. 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 사실을 이용해서 
#  6. 마지막줄이랑 마지막줄 -1 줄 ascending함수 하면 되는거 아닌가? 
#  

# In[15]:


n = int(input())
s = []
new_s = []
for _ in range(n) :
    s.append(list(map(int,input().split())))

for i in range (n):
    new_s.append(s[n-2][i])
    new_s.append(s[n-1][i])
    
new_s.sort(reverse=True)
print(new_s[n-1])   

