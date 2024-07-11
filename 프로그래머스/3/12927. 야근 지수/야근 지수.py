import heapq

def solution(n, works):
    max_heap = [-num for num in works]
    heapq.heapify(max_heap)
    
    # m번 가장 큰 수에서 1씩 빼는 작업을 합니다.
    for _ in range(n):
        largest = -heapq.heappop(max_heap)  # 가장 큰 수를 꺼내고
        if largest > 0:  # 0보다 큰 경우에만 감소
            largest -= 1  # 그 수에서 1을 빼고
        heapq.heappush(max_heap, -largest)  # 다시 힙에 넣습니다.
    
    # 남은 요소들을 제곱하여 더합니다.
    answer = sum(num * num for num in max_heap)
    return answer