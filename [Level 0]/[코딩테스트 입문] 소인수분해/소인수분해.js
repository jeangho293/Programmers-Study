function solution(n) {
  let prime = 2;
  const result = new Set();

  while (n !== 1) {
    if (n % prime === 0) {
      n /= prime;
      result.add(prime)
    } else {
      prime++;
    }
  }
  return [...result];
}