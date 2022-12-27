function solution(t, p) {
  const pLength = p.length - 1;
  let count = 0;
  for (let i = 0; i < t.length - pLength; i++) {
    if (t.substring(i, pLength + i + 1) <= p) {
      count++;
    }
  }
  return count;
}
