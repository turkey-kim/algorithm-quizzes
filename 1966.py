# 백준 프린터큐 문제.

import sys

from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, x = map(int, sys.stdin.readline().split())
    que = list(map(int, sys.stdin.readline().split()))
    res = list()
    que = deque(que)
    target = que[x] # x번째의 변수를 따로 저장해둔다.
    que[x] = 0 # x번째의 수를 정확히 구분하기 위하여 0으로 저장한다.
    
    while que:
        M = max(que) #반복연산을 줄이기 위해 따로 변수로 최댓값을 저장.
        if M < target and (0 in que): # 0으로 저장한 x번째의 원래값 d가 큐 속의 최대값이 되는 경우를 고려하기 위해 작성.
            M = target  
            
        if que[0] >= M: # 아래는 기본 로직.
            y = que.popleft()
            res.append(y)
        elif que[0] == 0 and target >= M: # 큐 속 0번 인덱스가 x번 째 수일 경우의 연산(1)
            res.append(0)
            que.popleft()
        elif que[0] == 0 and target < M: # 큐 속 0번 인덱스가 x번 째 수일 경우의 연산(2)
            y = que.popleft()
            que.append(y)       
        else:
            y = que.popleft()
            que.append(y)

    print(res.index(0) +1) # 뽑힌 순서대로 저장된 배열에서 x번째 수가 저장된 순서 출력.


'''
    - 풀이:

가장 큰 수부터 뽑는 큐를 만듦.
그리고, 해당 큐에서 초기에 지정된 수는 몇번째로 뽑히는지에 대한 연산을 추가하고자 함.
이 경우 지정된 수가 정확히 몇번째에 뽑혔는지 분명히 하는 것이 중요했다.
파이썬에서 데이터는 변수 안에 직접 담기는 것이 아니라
변수에 의해 참조되기에, 이를 고려하며 코드를 짜는 것이 어려웠다.
예컨데 a= [1, 1, 1, 1, 4, 6, 7, 21, 1]이 선언되었다고 하자.
여기서 1을 담은 요소들은 '1'이라는 정수 데이터를 담고 있는 것이 아니라,
'1'이라는 정수 데이터가 저장된 메모리의 특정 주소를 참조하고 있다.
육안으로 a를 볼때는 각각의 1들이 존재하는 것처럼 보이지만, 실제로 1들은 하나의 1이다.
앞선 예시를 이 문제에 적용해본다면, 특정 1을 제대로 지정하는 것이 관건이다.
만약 큐a 속 인덱스3의 1을 선택한다고 할 때, 인덱스 3번의 1은 몇번 째에 뽑히는 건가.
이를 분명히 하기 위해서 여러 방법을 생각해보다가 해당 1을 절대로 쓰이지 않는 값인 '0'으로 저장했다.
이 방법을 끼워맞춰 작성하다 보니 코드가 길어졌다.

'''
