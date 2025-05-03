#!/usr/bin/env python
# coding: utf-8

#  # Q 
#  때는 2020년, 백준이는 월드나라의 한 국민이다. 월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다. (단 도로는 방향이 없으며 웜홀은 방향이 있다.) 웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다. 웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.
# 
# 시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다. 한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때, 출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다. 여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.

#  # A
#  
# 
#  일반적인 벨만 포드 알고리즘이 아닌 "음의 간선 사이클"이 존재하는지 여부를 구한다.
# 
# "도로"는 양방향이고 "웜홀"은 단방향임을 주의해서 입력받아야 한다.
#  

# In[9]:


import sys
from sys import stdin
input = stdin.readline


def bf():
      for i in range(n):
            for j in range(len(edges)):
                cur, next, cost = edges[j]
                if dist[next] > dist[cur] + cost:
                        dist[next] = dist[cur] + cost
                        if i == n - 1:
                              return True
    return False
                        
TC = int(input())

for _ in range(TC):
    n, m, w = map(int, input().split())
    edges = []
    dist = [1e9] * (n + 1)
    for i in range(m + w):
            s, e, t = map(int, input().split())
            if i >= m:
                  t = -t
            else:
                  edges.append((e, s, t))
            edges.append((s, e, t))
            
    if bf():
          print("YES")
    else:
          print("NO")

