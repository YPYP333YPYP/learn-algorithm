# 42586. 기능개발

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/42586)

| 난이도 | 완료 (명) |
| :----: | :-------: |
|   lv 2   |  53,741         |

## 설계
먼저 progresses 배열과 speeds 배열을 이용해서 작업 진도가 100이 되는데 걸리는 일수를 계산하고 배열에 저장한다.

이후 배열을 반복문으로 돌면서 배열의 [0] 값을 최댓값을 뜻하는 mx 변수에 저장하고 이후에 값들과 비교하면서 최댓값보다 작으면 cnt 변수를 증가시키며 최댓값보다 큰 경우 현재의 값을 최댓값으로 바꾸고 cnt 변수를 answer에 추가한다. 
### 시간 복잡도
반복문을 2번 돌리므로 2n이 된다. O(2n) -> O(n)
## 코드
```python
from math import ceil
def solution(progresses, speeds):
    answer = []
    slist= []
    for v in range(len(speeds)):
        slist.append(100 - progresses[v])
        slist[v] = ceil(slist[v] / speeds[v])

    cnt = 1
    mx = 0
    for v in range(len(slist)):
        if v == 0:
            mx = slist[v]
        else:
            if mx >= slist[v]:
                cnt +=1   
            else :
                mx = slist[v]
                answer.append(cnt)
                cnt = 1
        if v == len(slist)-1:
                answer.append(cnt)
    return answer
```

## 리팩토링
```python
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
```
기존의 풀이는 stack/queue 문제임에도 자료구조를 사용하여 풀지 않았는데 queue를 이용한 풀이이다. 


time 변수와 count 변수를 이용하여 하나의 기능이 개발 완료되면 넘어간 개발의 수만큼 count 변수를 증가 시킨다. 다 개발하지 못했는데 넘어가야 하는 상황이라면 count 값을 answer 배열에 추가하고 count 변수를 초기화한다. 모든 값이 pop되면 반복문이 종료되고 종료하면서 마지막 count 값을 answer에 추가한다.