function solution(n) {
  let answer = 1;
  let count = 1;
  if (n === 1) {
    return 1
  }
  while (true) {
    if (answer === n) {
      return count - 1;
    }
    if (answer > n) {
      break
    }
    answer *= count;
    count++;

  }
  return count - 2
}