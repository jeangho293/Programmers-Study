function solution(numbers) {
  const arrayNumbers = Array.from(numbers);
  let result = '';
  let english = '';
  let numberObjects = { one: '1', two: '2', three: '3', four: '4', five: 5, six: 6, seven: '7', eight: '8', nine: '9', zero: '0' };



  while(arrayNumbers.length > 0) {
    english += arrayNumbers.shift();
    if (numberObjects[english]) {
      result += numberObjects[english]
      english = ''
    }
  }
  return parseInt(result)
}