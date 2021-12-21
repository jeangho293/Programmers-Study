# 문제 :book:

## 피보나치 수

### 접근 방식

- `swap 방식`의 피보나치 구현
- 주의할 점은 피보나치의 규칙 중 0, 1, 1, 2, 3, 5 에서 0, 1, 1은 초기값 설정 필요

<hr>

```python
def solution(n):
    n1, n2 = 1, 1   # 피보나치 초기값 설정
    for i in range(n-2):
        temp = n1 + n2
        n1, n2 = n2, temp
    return temp % 1234567
```

<hr>

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/146882061-ea4de38e-7965-4232-adae-263f45918bef.png)
