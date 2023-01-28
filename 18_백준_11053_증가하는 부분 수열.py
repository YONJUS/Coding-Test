#!/usr/bin/env python
# coding: utf-8

#  # Q 
#  수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

#   # A 
#   
# 입력 받은 걸 set함수로 만들어서 그 길이를 재었다
#  

# In[5]:


n = int(input())
t_list= [0]*n
t_list= list(map(int,input().split()))
a= set(t_list)
print(len(a))
    

