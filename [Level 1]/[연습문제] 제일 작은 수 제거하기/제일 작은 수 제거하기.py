def solution(arr):
    if len(arr) > 1:            # 길이가 2 이상부터 적용된다.
        arr.remove(min(arr))    # list.remove()를 적용하여 해당 값을 삭제한다.
        return arr
    else:
        return [-1]