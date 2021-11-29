from collections import Counter


def solution(participant, completion):
    participant, completion = Counter(participant), Counter(completion)
    return (participant - completion).most_common()[0][0]

