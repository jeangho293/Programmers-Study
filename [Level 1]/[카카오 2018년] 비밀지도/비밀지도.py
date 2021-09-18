def solution(n, arr1, arr2):
    arr1 = [int(format(i, 'b')) for i in arr1]  # 정수를 2진수 문자열로 치환
    arr2 = [int(format(i, 'b')) for i in arr2]  # 정수를 2진수 문자열로 치환

    maps = []
    for i in range(n):
        temp = ''
        number = '0' * (n - len(str(arr1[i] + arr2[i]))) + str(arr1[i] + arr2[i])   # 정수로 합을 구한수 n개의 갯수에 맞춰서 0을 보충한다.

        for _number in number:  # 지도의 조건인 '0'인 아닌 경우에는 보물이 있는 곳
            if _number != '0':
                temp += '#'
            else:
                temp += ' '
        maps.append(temp)
    return maps