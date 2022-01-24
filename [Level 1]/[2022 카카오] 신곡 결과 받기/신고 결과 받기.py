from collections import defaultdict


def solution(id_list, report, k):
    report_dict = defaultdict(set)
    caution_dict = defaultdict(int)
    result = [0] * len(id_list)

    for i in set(report):
        report_people = i.split(' ')
        report_dict[report_people[0]].add(report_people[1])
        caution_dict[report_people[1]] += 1

    caution_list = set()
    for who in caution_dict.keys():
        if caution_dict[who] >= k:
            caution_list.add(who)

    for i in report_dict.keys():
        report_dict[i] = len(report_dict[i] & caution_list)

    for index, id in enumerate(id_list):
        if id in report_dict.keys():
            result[index] = report_dict[id]

    return result


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))