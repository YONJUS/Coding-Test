#!/usr/bin/env python
# coding: utf-8

#  # Q)
#  - 첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다. 후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

# # A) 
# 
# - 처음 입력받은 N 
# - 스텍에 피연산자 값을 넣고 -> 연산자를 만나면 숫자 두개를 pop하여 계산 
# - 소수점 둘째자리 round(2)는 .00이 출력이 안돼서 %.f2로 해야된다
# 
# 
# 

# In[3]:


N = int(input())
num_stack = [0]*N # N개만큼 받을 거니까 
word = input() #이후 받는 문자열 
stack = []


for i in range(N): 
    num_stack[i] = int(input())

for i in word:
    if 'A'<= i <='Z':
        stack.append(num_stack[ord(i)-ord('A')]) #알파벳 만나면 stack안에 저장
        #ord함수 : 문자 -> 아스키 코드 10진수 변환 
        
    else : 
        str2 = stack.pop()
        str1 = stack.pop() # 연산자를 만나면 스택 리스트의 마지막 항목 두개를 꺼냄
                           # str2가 뒤에 있는 숫자 str1이 앞에 있는 숫자(더 늦게 꺼냄)
            
        
        if i == '+': 
            stack.append(str1+str2)
        if i == '-': 
            stack.append(str1-str2)
        if i == '/': 
            stack.append(str1/str2)
        if i == '*': 
            stack.append(str1*str2)
print('%.2f' %stack[0])      
        

