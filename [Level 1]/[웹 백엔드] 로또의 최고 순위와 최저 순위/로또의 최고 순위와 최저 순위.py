def solution(lottos, win_nums):
    # 맞은 갯수에 대한 순위 dictionary
    collect_nums = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    # 와일드 카드 (0)의 갯수
    wild_card = lottos.count(0)

    # lottos와 win_nums의 교집합의 갯수
    win = len(set(lottos) & set(win_nums))

    return [collect_nums[win+wild_card], collect_nums[win]]