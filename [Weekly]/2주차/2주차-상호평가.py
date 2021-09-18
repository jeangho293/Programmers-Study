# 리스트의 요소 중 중복된 요소를 포함하여 개수를 세어주는 라이브러리
from collections import Counter

def solution(scores):
    length, answer = len(scores), ''

    # zip함수를 활용하여 행-열 순서를 열-행 순서로 리스트 교환
    for i, score in enumerate(list(zip(*scores))):
        self_score = score[i]

        # 스스로를 평가한 점수이며 평가점수 중 가장 낮거나 가장 높은 수일 경우
        if Counter(score)[self_score] == 1 and (self_score == min(score) or self_score == max(score)):
            result = int((sum(score) - self_score) / (length - 1))
        else:
            result = int(sum(score) / length)

        # 점수에 따른 학점
        if result >= 90:
            answer += 'A'
        elif result >= 80:
            answer += 'B'
        elif result >= 70:
            answer += 'C'
        elif result >= 50:
            answer += 'D'
        else:
            answer += 'F'

        return answer
