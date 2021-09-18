# n은 정수로 받아왔으므로 문자열로 정리해주는 작업이 필요하다.
def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse=True)))