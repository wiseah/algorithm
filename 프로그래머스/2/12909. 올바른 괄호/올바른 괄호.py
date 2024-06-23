def solution(s):
    stack = 0
    for i in s:
        if i == '(': # 왼쪽 괄호는 stack에 추가
            stack += 1
        else:
            if stack == 0: # 오른쪽 괄호부터 시작하는 경우
                return False
            stack -= 1 # 왼쪽 괄호 pop
    
    return stack == 0 # 순회가 끝났을 때 스택이 비었으면 True
