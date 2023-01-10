#!/usr/bin/env python
# coding: utf-8

# In[6]:


def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i,end = '')
        print()
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0 
        DFS(v + 1)

if __name__ == "__main__":
    n = int(input())
    ch=[0]*(n + 1)
    DFS(1)


# # 부분집합 구하기 (DFS) 
# 
# - 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램을 작성
# 
# - DFS 전위순회 방식으로 출력하는데 전위순회 자식 노드에서 왼쪽을 1, 오른쪽을 0으로 하였다. 그래서 방문한 1이 있는 인덱스를 출력한다.  
