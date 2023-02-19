function solution(lottos, win_nums) {
  const rank = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6};
  const zeroCounts = lottos.filter((lotto) => lotto === 0).length;
  const equalNumbers = lottos.filter((lotto) => win_nums.includes(lotto)).length
  return [rank[equalNumbers+zeroCounts] ,rank[equalNumbers]]
}