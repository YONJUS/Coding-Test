#!/usr/bin/env python
# coding: utf-8

#  # Q) 합이 같은 부분집합(DFS : 아마존 인터뷰)
#  
#  - n 개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때  
#  - 두 부분집합 합이 같으면 YES, 아니면 NO 출력 
# 

# # A) 
#  - 재귀함수를 통해 부분집합으로 만든 것의 합인 sum과, 그렇지 않은 부분집합의 합(total-sum) 의 변수를 만든다 
#  - 전체 원소 합을 total이라고 함 -> sum에다가 원소 누적 후, (total - sum) == sum이면 yes 출력 

# In[4]:


import sys

def DFS(L,sum): # L은 a리스트 원소의 각 인덱스 번호, sum은 부분집합의 원소들 누적
    if L == n : #종료 지점
        if sum == (total - sum):
            print("YES")
            sys.exit(0) #참인 경우 프로그램 종료
    else:
        DFS(L+1, sum+a[L]) #a list 부분집합을 sum에 더하기
        DFS(L+1, sum)
        
            

n = int(input())
a = list(map(int,input().split()))
total = sum(a)
DFS(0,0)
print("NO") #DFS 에서 YES에 안걸려서 프로그램 종료가 안 된 경우-> NO 


# In[ ]:




