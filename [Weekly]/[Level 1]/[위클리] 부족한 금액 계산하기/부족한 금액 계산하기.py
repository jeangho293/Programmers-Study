# 등차수열의 합
def solution(price, money, count):
    need_money = 0
    for i in range(1, count + 1):
        need_money += price * i

    return need_money - money if need_money > money else 0