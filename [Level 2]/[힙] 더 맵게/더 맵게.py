import heapq as heap

def solution(scoville, K):
    heap.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        try:
            first = heap.heappop(scoville)
            second = heap.heappop(scoville) * 2
            heap.heappush(scoville, first+second)
            cnt += 1
        except:
            return -1
    return cnt