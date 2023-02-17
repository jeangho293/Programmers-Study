function solution(n) {
  let sum = 0;
  for(let i=1; i < n**0.5; i++) {
    if (n % i === 0) {
      sum += 2;
    }
  }

  if (n**0.5 === parseInt(n**0.5)) {
    sum += 1
  }

  return sum;
}