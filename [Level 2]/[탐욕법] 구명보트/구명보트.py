from collections import deque


def solution(people, limit):
    boat, people = 0, deque(sorted(people))

    while people:
        if len(people) == 1:
            return boat + 1
        if people[0] + people[-1] > limit:
            people.pop()
        else:
            people.pop()
            people.popleft()
        boat += 1
    return boat