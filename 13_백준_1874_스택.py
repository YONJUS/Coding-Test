#!/usr/bin/env python
# coding: utf-8

# # Q)
# - 첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

# # A) 
# 
#  1) 첫 번째 입력한 수인 4 이하인 수를 모두 스택에 넣는다. stack = [1, 2, 3, 4]
# 
#  2) 스택의 가장 위 숫자와 첫 번째 수가 같으면 pop()으로 스택에서 꺼낸다. stack = [1 2]
# 
#  3) 동일하지 않으면 스택 수열을 만들 수 없으므로 NO를 출력한다.

# In[ ]:


i = 1 # 양의 정수의 최소
temp = True
stack = [] 
op = [] # + , - 

N = int(input())
for i in range(N):
    num = int(input())
    
    # num이하 숫자까지 스택에 넣기
    while i <= num:
        stack.append(i)
        op.append('+')
        i += 1

    # num이랑 스택 맨 위(=마지막) 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)

