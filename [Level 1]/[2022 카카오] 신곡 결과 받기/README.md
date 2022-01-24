# 문제 :book:

## 신고 결과 받기

### 접근 방식

- `dictionary`와 `set()` 타입을 활용하여 문제 풀이

<hr>

```python
from collections import defaultdict


def solution(id_list, report, k):
    report_dict = defaultdict(set)  # 초기 값은 set
    caution_dict = defaultdict(int) # 초기 값은 0
    result = [0] * len(id_list)

    for i in set(report):
        report_people = i.split(' ')
        report_dict[report_people[0]].add(report_people[1]) # 누가 신고했는지를 확인
        caution_dict[report_people[1]] += 1 # 신고당한 횟수

    caution_list = set()
    for who in caution_dict.keys():
        if caution_dict[who] >= k:  # k만큼 신고당했을 경우, 안내메일 전송
            caution_list.add(who)

    for i in report_dict.keys():
        report_dict[i] = len(report_dict[i] & caution_list) # 교집합으로 안내메일 받을 횟수

    for index, id in enumerate(id_list):
        if id in report_dict.keys():
            result[index] = report_dict[id]

    return result
```

<hr>

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/150670230-010a0985-6710-4278-9af1-c72293acc117.png)
