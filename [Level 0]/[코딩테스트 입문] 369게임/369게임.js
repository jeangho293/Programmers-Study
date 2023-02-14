function solution(order) {
  const orderArray = Array.from(String(order));
  return orderArray.filter((order) => {
    if (order === '3' || order === '6' || order === '9') {
      return order
    }
  }).length
}
