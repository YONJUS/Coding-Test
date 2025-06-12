# OOXXOXXOOO
n = int(input())
for _ in range(n):
    arr = input()
    cnt, ans = 0, 0
    for i in arr:
        if i == 'O':
            cnt+=1
            ans+=cnt
        else:
            cnt=0
    print(ans)