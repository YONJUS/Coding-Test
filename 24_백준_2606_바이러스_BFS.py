#!/usr/bin/env python
# coding: utf-8

#  # Q)
#  
#  신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 
# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

# BFS 사용
# 
# graph list -> 각 연결된 컴퓨터 확인 
# visited list -> 들린거는 true로 만듦 
# dfs로 순회하고, 컴퓨터 리스트가 갖고있는 요소를 i를 어팬드 

# In[1]:


from collections import deque

n = int(input()) #컴퓨터 대수 
connect = int(input()) #노드의 개수 
graph = [[] for i in range(n+1)]  #graph 리스트의 index를 이용해서 n개의 컴퓨터가 각각 연결된 컴퓨터를 확인할 수 있도록 한다_
visited = [False]*(n+1)
cnt = 0

for i in range(connect):
    s, e = map(int, input().split()) # start, end 
    # 네트워크 상 연결 : 양방향 , 바이러스는 양방향으로 전파될 수 있으므로 두 방향에 대한 정보를 기입한다
    graph[s].append(e)
    graph[e].append(s)

def bfs(graph, v):
    global cnt
    queue = deque([v])  #BFS는 deque 안에 리스트를 사용한다

    while queue:  #BFS는 큐 자료구조안에 모든 값이 없어질 때(queue == False) 까지 반복한다
        pop = queue.popleft()  #가장 먼저 기입된 요소를 pop 해주면서 체커 표시를 한다
        visited[pop] = True

        for i in graph[pop]:
            if visited[i]==False:
                visited[i] = True
                queue.append(i)  #체커 표시된 컴퓨터의 리스트가 갖고 있는 요소(i)를 큐 구조에 append 해준다
                cnt += 1  #체커 표시가 되어 있지 않은(큐 안에 삽입된 적이 없는) i 값만을 사용해서 cnt를 증가시켜준다
    print(cnt)

bfs(graph, 1)

