'''
풀이과정
cf) cnt = 작은 포식자가 먹는거 ans = 
1. 포식자 중에서 더 작은 애들이 먹을 수 있는건: 더 큰 애들도 먹을 수 있음-> 굳이 계산할 필요가 읍다
2-1) 둘이 sort한 다음에, pop하면서 피식자 집합을 뒤에서부터 훑음(작은거부터)
2-2) 훑을 때 피식자 중에서 큰거 만나면 break
'''
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    po = list(map(int, input().split()))
    pi = list(map(int, input().split()))
    po = sorted(po,reverse=True)
    pi = sorted(pi,reverse=True)
    cnt, ans = 0, 0
    while(po):
        x = po.pop()
        l = len(pi)
        for i in range(l):
            if x > pi[-1]:
                cnt+=1
                pi.pop()
            else: break
        ans += cnt
    print(ans)

'''
two-pointer 풀이법
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    po = sorted(map(int, input().split()))
    pi = sorted(map(int, input().split()))
    
    i = j = ans = 0
    while i < a and j < b:
        if po[i] > pi[j]: # 피식자[j]보다 큰 포식자자[i]를 찾으면면
            j += 1
            ans += a - i  # 이후 모든 값이 더 크므로 한 번에 누적
        else:
            i += 1
    print(ans)
'''
