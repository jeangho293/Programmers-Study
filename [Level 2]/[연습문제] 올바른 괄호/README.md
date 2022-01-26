# 문제 :book:

## 올바른 괄호

### 접근 방식

- 자료구조 `stack`을 활용한 접근법
- `try ~ except`으로 해당되는 key가 없을 경우, 예외처리로 빠른 탈출


<hr>

```python
bracket = {'(': ')'}    # 알맞는 괄호를 찾기 위한 딕셔너리

def solution(s):
    stack = []
    for i in s:
        try:
            if stack and bracket[stack[-1]] == i:   # stack이 존재하고 짝이 맞을 경우
                stack.pop() # 맞은 짝에 대해서 pop() 연산
            else:   # 그렇지 않을 경우 
                stack.append(i)
        except: # keyError의 경우 짝이 맞지 않는다는 의미로 for문 break
            break
    
    return stack == [] # stack이 비어있으면 모두 짝이 맞았다는 의미
```

<hr>

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/151120167-867c67d6-df30-455c-8437-6cdf9bc728e9.png)