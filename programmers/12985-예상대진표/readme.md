# 12985.예상대진표

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/12985#)

| 난이도 | 완료 (명) |
| :----: | :-------: |
|   lv 2  |    16,934     |

## 설계
N만큼의 크기를 가진 리스트를 생성한 후 2명씩 짝을 지어 리스트를 만들었을 때 리스트 안에 a,b가 모두 포함되면 서로가 만난다고 표현할 수 있다.
이것을 이용해서 크기를 2의 n승 만큼 리스트를 분할하고 a,b 값이 포함되어 있는지 체크한다. 

### 시간 복잡도
만든 list_chunk의 시간 복잡도가 O(n)이며, slist 생성 시 O(n)이기 때문에 시간 복잡도는 O(n)을 넘지 않는다.
## 코드
```python
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def solution(n,a,b):
    answer = 0
    slist = [ x for x in range(1,n+1)]
    cnt = 0
    i = 2
    while i > 0:
        vlist = list_chunk(slist, i)
        for v in vlist:
            if a in v and b in v:
                i = 0
            
        cnt +=1
        i *=2
    answer = cnt   
    return answer
```

## 리팩토링
```python
def solution(n,a,b):
    answer = 0
    
    while a != b:
        answer += 1
        a = (a+1) // 2
        b = (b+1) // 2
    return answer
```
조금 더 간단한 방법으로 2로 나누면서 몫이 같아질때 까지 내용을 반복하고 반복한 만큼이 answer이 되는 경우이다.
