function solution(my_string) {
  const array = Array.from(my_string);
  let result = ''
  for(let i=0; i<array.length; i++) {
    if(array[i].charCodeAt(0) >= 97) {
      result += array[i].toUpperCase();
    } else {
      result += array[i].toLowerCase();
    }
  }
  return result
}
