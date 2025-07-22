function solution(brown, yellow) {
  const total = brown + yellow;
  for (let row = 0; row < parseInt(Math.sqrt(total)) + 1; row++) {
    if (total % row == 0) {
      col = total / row;
      if (brown == 2 * (row + col - 2)) {
        return [col, row];
      }
    }
  }
}
