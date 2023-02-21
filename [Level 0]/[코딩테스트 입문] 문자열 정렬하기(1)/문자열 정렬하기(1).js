function solution(my_string) {
  my_string = Array.from(my_string);
  my_string.sort()
  return my_string.reduce((acc, curr) => {
    if (Number.isInteger(Number(curr))) {
      acc.push(Number(curr))
    }
    return acc;
  }, [])
}