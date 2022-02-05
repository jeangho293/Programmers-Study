# 문제 :book:

## 신규 아이디 추천

### 접근 방식

- `import re` 내장 라이브러리를 활용하여 문자열 다루기

<hr>

```python
import re


def solution(new_id):
    # 1단계 --> 모든 문자를 소문자로 치환한다.
    new_id = new_id.lower()

    # 2단계 --> 조건에 맞는 알파벳, 숫자, 특수 문자만 추출
    new_id = ''.join(re.findall('[0-9a-z-._]', new_id))

    # 3단계 --> 연속된 마침표(.)를 하나로 바꾼다.
    new_id = re.sub('[.]+', '.', new_id)

    # 4단계 --> 처음과 끝의 마침표(.)를 지운다.
    new_id = new_id.strip('.')

    # 5단계 --> 빈 문자열일 경우, "a를 대입"
    if new_id == '': new_id = "a"

    # 6단계 --> 16글자이상일때 15글자로 줄이고 마지막 마침표(.) 제거
    if len(new_id) > 15:
        new_id = new_id[:15].rstrip('.')

    # 7단계 --> 2글자 이하일 경우 마지막 글자를 추가
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))

    return new_id

```

<hr>

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/152632644-1aac6fa0-4b60-4f3e-b5a0-96803a95a88a.png)
