function solution(array) {
  const maxNumber = Math.max(...array);
  return [maxNumber, array.indexOf(maxNumber)]
}
