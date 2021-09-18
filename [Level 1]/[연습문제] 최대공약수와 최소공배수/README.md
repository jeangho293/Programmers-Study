# 문제 :book:

## 최대공약수와 최소공배수

### 접근 방식

- 파이썬 내장 라이브러리인 __import math__ 는 최대공약수를 쉽게 구할 수 있는 함수가 있다.

- 최소공배수 = (A * B) / GCD(A * B)

<hr>

```python
import math
def solution(a, b):
    GCD = math.gcd(a, b)    # 최대공약수
    LCD = (a * b) // GCD    # 최소공배수
    return [GCD, LCD]
```

<hr>

## 실행 결과

![img.png](img.png)