# n의 조건이 1000000이므로 일반적인 소수 찾기로는 효율성 문제가 있음
# 에라토스테네스의 체 활용

def solution(n):
    Prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if Prime[i]:
            for j in range(i * i, len(Prime), i):
                Prime[j] = False

    return Prime[2:].count(True)