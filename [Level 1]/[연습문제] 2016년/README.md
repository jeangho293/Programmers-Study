## 쉬운 문제

`datetime` 라이브러리를 활용하여 문제 풀이


```python
from datetime import datetime

def solution(a, b):
    return (datetime(2016,a,b).strftime('%A').upper()[:3])
```

<hr>

## 실행 결과

![img.png](img.png)