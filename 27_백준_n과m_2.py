from itertools import combinations
n, m = map(int,input().split())
answer = []
arr = [i for i in range(1,n+1)]
res = list(combinations(arr, m))
for item in res:
    answer.append(list(item))  
for i in answer:
    print(*i)
