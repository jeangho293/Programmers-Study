bracket = {'(': ')'}


def solution(s):
    stack = []
    for i in s:
        try:
            if stack and bracket[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)
        except:
            break

    return stack == [];