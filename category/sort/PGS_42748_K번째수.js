function solution(array, commands) {
    var answer = [];
    for (let i = 0; i < commands.length ;i++){
        const sliced_array = array.slice(commands[i][0]-1, commands[i][1]);
        sliced_array.sort((a,b)=> a-b);
        answer.push(sliced_array[commands[i][2]-1]);
    }

    return answer;
}

//다른 풀이
function solution(array,commands){
  return commands.map(command => {
    const [sPosition, ePosition, position] = command
    const newArray = array.filter((value,fIndex) => fIndex >= sPosition - 1 && fIndex <= ePosition - 1).sort((a,b)=>a-b)
    return newArray[position-1]
  })
}