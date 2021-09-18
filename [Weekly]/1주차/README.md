# 문제 :book:

## 1주차 - 부족한 금액 계산하기


### 접근 방식

- 등차수열 합의 규칙을 보이므로 for문으로 해결.
- **sum([])** 방식으로 코드를 줄일 수 있음.

<hr>

```python
def solutoin(price, money, count):
    need_money = 0
    for i in range(1, count + 1):
        need_money += price * i  # 등차수열의 합

    return need_money - money if need_money else 0
```