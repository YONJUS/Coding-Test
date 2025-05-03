#!/usr/bin/env python
# coding: utf-8

#  # Q) 
#  - 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

#  # A) 
#  - 백트래킹을 하면서 그 리스트의 합이 s와 같은 것을 만날때마다 cnt에 +1을 해준 뒤 마지막에(인덱스 값이 >=n인 경우) 프린트를 한다. 
#  

# In[1]:


n, s = map(int, input().split()) # n은 정수의 개수 
arr = list(map(int, input().split()))
cnt = 0

def subset_sum(idx, sub_sum):
    global cnt

    if idx >= n: #index가 정수의 개수보다 크거나 같으면 리턴 
        return

    sub_sum += arr[idx] # sub_sum에 array인덱스 값을 더한다 

    if sub_sum == s: # 그 값이 설정한 s와 같으면 
        cnt += 1 # 카운트를 하나 더한다 
    
    #백트래킹
    subset_sum(idx+1, sub_sum) # 현재 arr[idx]를 선택한 경우의 가지
    subset_sum(idx+1, sub_sum - arr[idx])  # 현재 arr[idx]를 선택하지 않은 경우의 가지

subset_sum(0, 0)
print(cnt)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




