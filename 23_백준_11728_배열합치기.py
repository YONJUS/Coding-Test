#!/usr/bin/env python
# coding: utf-8

#  # Q
#  - 문제
# 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.
# 
#  - 입력
# 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)
# 
# 둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.
# 
#  - 출력
# 첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.

#  # A 
#  
# 투포인터를 활용해서 입력
#  

# In[5]:


n, m = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
answer = []
a_start = 0
b_start = 0
while a_start < n or b_start<m:
    
    if b_start >= m or (a_start < n and a[a_start] <= b[b_start]):
        answer.append(a[a_start])
        a_start += 1
    else:
        answer.append(b[b_start])
        b_start += 1
        
print(' '.join(list(map(str,answer))))

