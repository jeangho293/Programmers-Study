from itertools import combinations


def Prime_Search():
    prime = [True] * 3001

    for i in range(2, int(3001 * 0.5) + 1):
        if prime[i]:
            for j in range(i * i, 3001, i):
                prime[j] = False
    return prime


def solution(nums):
    nums = list(map(sum, combinations(nums, 3)))
    _prime = Prime_Search()

    return len([num for num in nums if _prime[num]])
