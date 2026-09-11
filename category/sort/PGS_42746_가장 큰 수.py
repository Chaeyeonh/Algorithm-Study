
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

#다른 풀이
import functools

def comparator(a,b):
    t1= a + b
    t2 = a-b
    return (int(t1)-int(t2)) - (int(t1)-int(t2))

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key = functools.cmp_to_key(comparator), reverse = True)