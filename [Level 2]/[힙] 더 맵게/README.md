# 문제 :book:

## 더 맵게

### 접근 방식

- `최소 힙`을 활용한 문제
- 매 순간마다 최소값을 보장해야 하기 때문에 파이썬 내장 라이브러리 `import heapq`를 활용한다.

<hr>

```python
import heapq as heap

def solution(scoville, K):
    heap.heapify(scoville)  # 최소 힙으로 정렬
    cnt = 0 
    while scoville[0] < K: # 힙정렬시 0번 인덱스는 최소값이 보장된다.
        try:
            first = heap.heappop(scoville) # 첫번째 최솟값
            second = heap.heappop(scoville) * 2 # 두번째 최솟값
            heap.heappush(scoville, first+second) # 최소힙을 보장한 heappush
            cnt += 1
        except: # scoville의 원소가 하나도 없을 경우, K이상으로 만들 수 없다.
            return -1
    return cnt
```

<hr>

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/150959785-aca6e3b9-2210-4dcb-aea7-9670ed12ef91.png)
