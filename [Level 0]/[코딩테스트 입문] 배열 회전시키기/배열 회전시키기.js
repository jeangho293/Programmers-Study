function solution(numbers, direction) {
  if (direction === "right") {
    const swap = numbers.pop();
    numbers.unshift(swap)
  } else {
    const swap = numbers.shift();
    numbers.push(swap);
  }

  return numbers;
}
