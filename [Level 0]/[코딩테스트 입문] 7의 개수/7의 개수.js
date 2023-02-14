function solution(array) {
  let count = 0;
  const newArray = Array.from(array.join(""));
  newArray.forEach((number) => {
    if (number === '7') {
      count += 1
    }
  })
  return count
}