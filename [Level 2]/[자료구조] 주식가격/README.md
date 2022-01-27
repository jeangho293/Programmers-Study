# 문제 :book:

## 주식가격

### 접근 방식

- `deque`를 활용하안 `queue`방식의 문제 풀이

<hr>

```python
from collections import deque

def solution(prices):
    result = []
    prices = deque(prices)  # deque 형식으로 변환
    
    while prices:
        price = prices.popleft()
        cnt = 0
        for next_price in prices:   
            if next_price < price: # 해당 가격이 다음 가격보다 낮을 경우
                cnt += 1
                break
            cnt += 1
        result.append(cnt)
    return result
```

<hr>

## 실행 결과
![image](https://user-images.githubusercontent.com/84619866/151333201-fbefec4b-3da6-4a43-85cc-e02ea94bd432.png)
