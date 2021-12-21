# 문제 :book:

## 소수 만들기

### 접근 방식

- `에라토스테네스의 체`를 통한 소수 검출
- `combinations` 메소드를 통한 조합 

<hr>

```python
from itertools import combinations


def Prime_Search():
    prime = [True] * 3001

    for i in range(2, int(3001 * 0.5) + 1):
        if prime[i]:
            for j in range(i * i, 3001, i):
                prime[j] = False
    return prime


def solution(nums):
    nums = list(map(sum, combinations(nums, 3)))
    _prime = Prime_Search()

    return len([num for num in nums if _prime[num]])
```

<hr>

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/146954766-7ab95f3e-490f-4936-b37c-5d39e53acc3b.png)
