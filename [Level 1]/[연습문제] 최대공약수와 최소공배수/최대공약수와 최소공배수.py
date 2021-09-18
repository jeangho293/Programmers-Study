import math
def solution(a, b):
    GCD = math.gcd(a, b)    # 최대 공약수
    LCD = (a * b) // GCD    # 최소 공배수
    return [GCD, LCD]