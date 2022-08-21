#백준 1541(greedy)

import sys

a = sys.stdin.readline().split('-')
res = 0

for i in a[0].split('+'):
    i = int(i)
    res += i
for i in a[1:]:
    for j in i.split('+'):
        j = int(j)
        res -= j

print(res)
    
    

'''
풀이:
최소값 만드는 로직은 다음과 같다.
마이너스 기호가 나올 때마다 그 뒤에 바로 괄호를 열기.
다시 한번 마이너스 기호가 나오기 직전에 괄호 닫기.
마이너스 기호가 다시 한번 나온다면 위의 과정 반복.


해당문제는 구현력 때문에 풀이를 살펴봄.
입력받은 스트링을 +,- 기호를 기준으로 쪼개어 정수처리하는 구현력이 부족했다.

'''
