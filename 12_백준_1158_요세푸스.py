#!/usr/bin/env python
# coding: utf-8

# # Q) 
# 
# - 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# In[1]:


N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]    # 처음에 원에 앉아있는 사람 배열

answer = []   # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for _ in range(N):
    num += K-1  
    if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(arr)
 
    answer.append(str(arr.pop(num)))


    
print("<",", ".join(answer)[:],">", sep='') # ,앞에 answer array를 순서대로 넣음

