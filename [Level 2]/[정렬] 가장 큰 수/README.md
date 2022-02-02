# 문제 :book:

## 가장 큰 수

### 접근 방식

- 문자열도 대소비교를 아스키코드로 가능하므로 같은 숫자를 3번씩 반복했을 때, 가장 큰 문자열이 가장 큰 숫자이므로 이러한 방식으로 가장 큰 수를 구한다.

<hr>

```python
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
```

<hr>

## 실행 결과
![image](https://user-images.githubusercontent.com/84619866/152174695-0d37cb40-8b31-4b95-bc4b-6db90c836e9f.png)


