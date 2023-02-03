#!/usr/bin/env python
# coding: utf-8

#  # Q) 
#  
# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

#  # A) 
#  
#  1) start point, end point(원소의 인덱스)를 0으로 시작해서, 
#  
#  2) tmp가 요구한 값보다 작으면 end point를 +1을함 
#  
#  3) tmp가 m과 같으면 cnt에 +1을하고 start point에 +1을한다 
#  
#  4) tmp가 m보다 크면 tmp에 start point의 숫자를 뺀 뒤, start point에 +1을 함 
#  

# In[8]:


n,m = map(int,input().split())
num = list(map(int,input().split()))
tmp = num[0]
cnt, sp, ep = 0, 0, 0

while True:
    if tmp < m: # 부분합이 m보다 작으면 end point +1 
        ep += 1
        if ep >= n: #end point가 n보다 크면 while문 빠져나감 
            break
        tmp += num[ep]
    elif tmp == m :
        cnt += 1
        tmp -= num[sp]
        sp += 1
    else: 
        tmp -= num[sp]
        sp += 1
print(cnt)

