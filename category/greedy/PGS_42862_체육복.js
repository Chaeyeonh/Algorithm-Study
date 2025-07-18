function solution(n, lost, reserve) {
  //1. set으로 변환
  const lostSet = new Set(lost);
  const reserveSet = new Set(reserve);

  //2. 자기 자신에게 빌려줄 수 있는 경우 제거
  for (const x of [...lostSet]) {
    //스프레드 연산자: Set의 모든 요소를 풀어 새 배열 만듦. Set을 수정하면서 안전히 순회하기 위해
    if (reserveSet.has(x)) {
      lostSet.delete(x);
      reserveSet.delete(x);
    }
  }

  //3. 기본 수업 가능한 학생 수
  let answer = n - lostSet.size;

  //4. 인접 학생에게 그리디하게 빌려주기
  for (const r of [...reserveSet].sort((a, b) => a - b)) { //정렬하는 콜백함수 sort. a-b<0이면 a가 더 작은 값이 앞에: 오름차순
    if (lostSet.has(r - 1)) {
      lostSet.delete(r - 1);
      answer++;
    } else if (lostSet.has(r + 1)) {
      lostSet.delete(r + 1);
      answer++;
    }
  }
  return answer;
}
