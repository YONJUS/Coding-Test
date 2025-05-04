x = int(input())
answer = 0
while(x>0):
    answer += x%2
    x = x//2
print(answer)