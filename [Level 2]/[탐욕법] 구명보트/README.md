# 문제 :book:

## 구명보트

### 접근 방식

- `deque`를 활용하안 `queue`방식의 문제 풀이
- `sorted()`로 **오름차순** 정렬
- 오름차순 정렬이 되었을 경우, 가장 첫번째 원소와 마지막 원소의 합의 `limit`을 넘는지를 확인한다
  - 두 사람의 합이 limit보다 작거나 같을 경우, 둘 다 태워서 보내면된다.
  - 두 사람의 합이 limit보다 클 경우, 가장 무거운 사람 한명만 태워서 보낸다.

<hr>

```python
from collections import deque


def solution(people, limit):
    boat, people = 0, deque(sorted(people))

    while people:
        if len(people) == 1:
            return boat + 1
        if people[0] + people[-1] > limit:  # limit를 넘을 경우, 가장 무거운 사람 혼자 태워보낸다.
            people.pop()
        else:   # limit보다 작거나 같을 경우, 둘 다 태워서 보낸다.
            people.pop()
            people.popleft()
        boat += 1
    return boat
```

<hr>

## 실행 결과
![image](https://user-images.githubusercontent.com/84619866/151783642-a409366e-942b-4c6f-8648-483d3ef7647c.png)

