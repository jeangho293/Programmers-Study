def solution(n):
    answer = set()  # 정수 제곱근일 경우 중복값을 제거하기 위함.
    for i in range(1, int(n ** 0.5) + 1):   # 제곱근으로 판별 시, 더 효율적이다.
        if n % i == 0:
            answer.add(i)
            answer.add((n // i))

    return sum(answer)