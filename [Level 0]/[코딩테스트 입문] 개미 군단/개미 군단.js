function solution(hp) {
  const ant = [0, 0, 0]

  // 장군개미
  ant[0] = parseInt(hp / 5)
  hp -= ant[0] * 5

  // 병정개미
  ant[1] = parseInt(hp / 3)

  // 일개미
  ant[2] = hp - ant[1] * 3

  return ant.reduce((acc, curr) => acc + curr, 0)
}