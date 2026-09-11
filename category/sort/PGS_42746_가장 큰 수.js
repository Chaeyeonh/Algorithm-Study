
function solution(numbers) {
    var answer = numbers.map(v=>v+'') // 숫자 배열을 문자열 배열로. 
                        .sort((a,b) => (b+a)*1 - (a+b)*1)
                        .join('');

    return answer[0]==='0'?'0':answer;
}