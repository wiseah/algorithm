from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit: # 최댓값과 최솟값 묶어서 보트태움
            answer += 1
            people.pop()    #최소 빼내고
            people.popleft()    #최대 빼내고
        else:
            answer += 1
            people.popleft()
            
    if people:  #people에 1명 남아있는 경우 처리
        answer += 1
                
    return answer

# Greedy 알고리즘을 어떻게 사용할 것인가가 핵심인 문제. 보트를 가장 적은 횟수로 사람들을 이동시키려면 제일 무거운 사람, 제일 가벼운 사람을 같이 묶어서 처리해야한다는 게 핵심 아이디어다.

# people 리스트를 덱으로 만든 후 내림차순 정렬
# 무거운 사람(왼쪽)과 가벼운 사람(오른쪽)을 인덱스로 매칭
# 합이 보트 무게보다 가벼우면 둘 빼냄
# 보트 무게보다 무거우면 무거운 사람만 빼냄