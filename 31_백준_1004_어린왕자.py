'''
풀이과정:
왜 지나야만 하는지, 왜 안 지나도 되는지 생각해봄 -> 점이 원 안에 포함되어있으면 무조건 지나야 되는구먼
+ end point를 또 다른 start point라고 생각하고 각자 무조건 지나야 되는 원의 개수를 센다음에 합치면 되잖슴~

1) start point나 end point가 input으로 받는지 원에 포함되는 지 판단 후
2) xor연산 참일때 cnt +=1 
왜 xor인가? 
True ^ False 또는 False ^ True는 True지만, True ^ True와 False ^ False는 False입니다.
따라서 딱 하나만 행성계 내부에 있는 경우만 count합니다.

'''
t  = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int,input().split())
    n = int(input())
    cnt = 0 
    for _ in range(n):
        tmp_x, tmp_y, r = map(int,input().split())
        d_s = (x1-tmp_x)**2+(y1-tmp_y)**2
        d_e = (x2-tmp_x)**2+(y2-tmp_y)**2
        r = r**2
        if (d_s <= r) ^ (d_e <= r):
            cnt += 1
    print(cnt)
    