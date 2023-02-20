function solution(my_string) {
  const arrayString = my_string.split('');
  const duplicatedAlpha = {};
  const result = []

  while (arrayString.length > 0) {
    let shift = arrayString.shift()
    if (!duplicatedAlpha[shift]) {
      duplicatedAlpha[shift] = true;
      result.push(shift)
    }

  }
  return result.join('');
}