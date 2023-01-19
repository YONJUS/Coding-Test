#!/usr/bin/env python
# coding: utf-8

#  # Q ) 
# - 총 N개의 문자열로 이루어진 집합 S가 주어진다. 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

#  # A) 
#  
#  - N개 입력받은 뒤 리스트에 넣고, M개 입력 받은 뒤 새로운 리스트에 넣은 뒤 비교하는 방법이 있으나, 이는 시간 복잡도가 높다
#  - set이나 dictionary 사용 
#  
#  
#  
#  

# In[2]:


N, M = map(int, input().split()) # n,m입력 받고 

s = set([input() for _ in range(N)]) #s = 문자열 n번 받기
cnt = 0 
for _ in range(M): #m번 문자 받아서 받을때마다 s에 있나 확인 -> 있으면 +1, 없으면 0
    t = input()
    if t in s:
        cnt += 1
print(cnt)

