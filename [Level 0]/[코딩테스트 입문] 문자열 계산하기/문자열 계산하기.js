function solution(my_string) {
  my_string = my_string.split(' ')
  let sum = parseInt(my_string.shift())
  while (my_string.length > 0) {
    let shift = my_string.shift()

    if (shift === '+') {
      sum += parseInt(my_string.shift())
    } else if (shift === '-') {
      sum -= parseInt(my_string.shift())
    }
  }
  return  sum
}