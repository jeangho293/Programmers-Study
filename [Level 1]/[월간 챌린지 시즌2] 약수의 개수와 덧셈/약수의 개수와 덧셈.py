# 약수의 개수가 짝수면 더하고, 홀수면 뺀다.
# sqrt() 또는 a ** b를 이용
def solution(left, right):
    answer = 0
    for number in range(left, right + 1):

        # 약수의 개수가 홀수인것은 제곱근이 정수만 성립된다.
        if number ** 0.5 != int(number ** 0.5):
            answer += number
        else:
            answer -= number
    return answer