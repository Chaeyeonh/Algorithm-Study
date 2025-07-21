function solution(number, k) {
  let answer = "";
  const stack = [];

  for (let i = 0; i < number.length; i++) {
    const num = number[i];

    while (stack.length > 0 && stack[stack.length - 1] < num && k > 0) {
      stack.pop();
      k--;
    }
    stack.push(num);
  }

  if (k > 0) {
    stack.splice(stack.length - k, k); //배열에서 원하는 인덱스부터 k개를 제거하는 메서드
  }

  answer = stack.join("");
  return answer;
}
