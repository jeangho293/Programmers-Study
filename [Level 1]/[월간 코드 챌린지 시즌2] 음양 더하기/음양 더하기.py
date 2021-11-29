def solution(absolutes, signs):
    for i, v in enumerate(signs):
        if not v:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)