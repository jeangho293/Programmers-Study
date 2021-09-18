def solution(n):
    return ''.join(list(map(lambda x: '수' if x % 2 == 1 else '박', range(1, n+1))))