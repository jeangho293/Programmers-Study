function solution(s) {
  const array = s.split(' ');
  const result = [];

  while (array.length > 0) {
    if (Number.isInteger(Number(array[0]))) {
      result.push(array.shift())
    } else {
      result.pop()
      array.shift()
    }
  }

  return result.reduce((acc, curr) => acc + Number(curr), 0)
}