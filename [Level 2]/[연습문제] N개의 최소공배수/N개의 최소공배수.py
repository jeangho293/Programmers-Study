from math import gcd


def solution(array):
    result = 1
    for i in array:
        GCD = gcd(result, i)
        result *= i // GCD
    return result