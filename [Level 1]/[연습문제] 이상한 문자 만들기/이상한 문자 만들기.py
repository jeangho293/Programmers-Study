def solution(s):
    cnt = 0
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
            cnt = 0
        else:
            if cnt % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            cnt += 1
    return answer