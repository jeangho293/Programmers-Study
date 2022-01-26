# 문제 :book:

## 최댓값과 최솟값

### 접근 방식

- `split`을 활용하여 공백을 기준으로 list 치환
- `map`을 활용하여 각 원소를 int 형으로 전환
- `sorted`를 통해서 오름차순 정렬
  - `sorted()`는 **반환값이 존재한다.**
  - 'a.sort()'는 **반환값이 존재하지 않는다.**

<hr>

```python
def solution(s):
    s = sorted(list(map(int, s.split())))
    return f'{s[0]} {s[-1]}'
```

<hr>

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/151119060-7016ad58-ec05-42c6-ae05-beea04874c1e.png)
