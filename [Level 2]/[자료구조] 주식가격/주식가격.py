from collections import deque


def solution(prices):
    result = []
    prices = deque(prices)

    while prices:
        price = prices.popleft()
        cnt = 0
        for next_price in prices:
            if next_price < price:
                cnt += 1
                break
            cnt += 1
        result.append(cnt)
    return result