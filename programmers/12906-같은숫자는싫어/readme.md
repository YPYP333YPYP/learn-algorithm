# 12906. 같은숫자는싫어

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/12906)

| 난이도 | 완료 (명) |
| :----: | :-------: |
|  lv.1  |  56,355   |

## 설계
주어진 arr 배열에서 첫 번째 문자열은 answer에 삽입하고 이후에 분기점을 만들어 answer 배열에 값이 같을 경우는 pass하고 값이 같지 않을 경우 즉 연속하지 않을 경우는 answer 배열에 값을 추가한다.

### 시간 복잡도
arr 배열의 크기만큼 반복문을 돌리기 때문에 O(n)이다.

## 코드
```python
def solution(arr):
    answer = []
    cnt = 0
    answer.append(arr[0])
    for v in range(1,len(arr)):        
        if answer[cnt] == arr[v]:
            pass
            
        else:
            answer.append(arr[v])
            cnt+=1
            
    return answer
```

## 리팩토링
``` python
def solution(arr):
    answer= []
    for v in arr:
        if len(answer) == 0 or answer[-1] != v:
            answer.append(v)
            
    return answer

```
기존의 풀이와 다르게 stack의 개념을 사용했고 결국 answer 배열에 마지막 값과 arr 배열의 현재의 값을 비교하는 것이기 때문에 answer[-1]으로 접근한다. 또한 기존에는 answer에다가 arr[0]의 값을 추가하는 코드가 있었다면 if 문의 조건문으로 해당 코드를 효율적으로 작성할 수 있다. 