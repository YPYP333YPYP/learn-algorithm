# 12909. 올바른 괄호

[링크](https://school.programmers.co.kr/learn/courses/30/lessons/12909)

| 난이도 | 완료 (명) |
| :----: | :-------: |
|   lv 2   |    36,916       |

## 설계
기본적인 메커니즘은 "(" 이 들어올때는 추가를, ")"이 들어올때는 기존의 stack의 값을 제거하여 로직이 끝났을 때 stack이 비어 있으면 True, stack에 값이 있으면 False를 반환한다. 추가적으로 stack[0]에 ")"이 들어오는 경우는 False를 반환하도록 한다.

### 시간 복잡도
주어진 배열 s만큼 반복문을 돌리기 때문에 O(n) 이다.

## 코드
```python
def solution(s):
    answer = True
    stack = []
    for v in s:
        if len(stack) == 0 and v == ")":
            return False
        elif v == "(":
            stack.append(v)
        elif v == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
            
    if len(stack) == 0:
        asnwer = True
    else: 
        answer = False
    return answer
    
```


## 리팩토링
```python
def solution(s):
    stack = []
    for c in s:
        if c=='(':
            stack.append(c)
        elif not stack or stack.pop()!='(':
                return False
    return False if stack else True
```
stack이 비어있는 것을 python의 특성을 잘 살려 변수 그 자체를 조건문의 조건으로 제시함으로써 코드를 효율적으로 작성할 수 있다. 