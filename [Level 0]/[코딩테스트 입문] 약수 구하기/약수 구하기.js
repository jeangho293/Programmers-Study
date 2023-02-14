function solution(n) {
  const answer = new Set();
  for(let i=1; i<=n**0.5; i++) {
    if (n % i === 0) {
      answer.add(i);
      answer.add(n / i);
    }
  }
  return Array.from(answer).sort((a,b) => a-b);
}
