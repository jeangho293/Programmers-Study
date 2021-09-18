# stack 을 활용하여 풀이

def solution(arr):
    stack = []

    for i in arr:
        try:
            if stack[-1] != i:
                stack.append(i)
        except:
            stack.append(i)
    return stack