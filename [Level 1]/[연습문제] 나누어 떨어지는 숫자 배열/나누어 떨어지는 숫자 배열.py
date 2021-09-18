def solution(arr, divisor):
    result = [number for number in sorted(arr) if number % divisor == 0]
    return [-1] if not result else result