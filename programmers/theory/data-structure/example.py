# 배열 
arr = [1,2,3,4]


# 벡터
v = []
v.append((123,456))
v.append((789, 987))


# 스택
s = []
s.append(123)
s.append(456)
s.append(789)

while (len(s)) > 0:
    print(s[-1]) # 가장 마지막에 입력된 값 
    s.pop(-1) # pop 메서드는 가장 맨 뒤에 값을 추출


# 큐
from collections import deque
q = deque()
q.append(123)
q.append(456)
q.append(789)

while len(q) > 0:
    print(q.popleft()) # pop 메서드 또한 존재하는데 pop은 가장 오른쪽 값을, popleft는 가장 왼쪽 값을 추출한다. 



# 우선순위 큐
import heapq

pq = []
heapq.heappush(pq,456)
heapq.heappush(pq,123)
heapq.heappush(pq,789)

while len(pq) > 0:
    print(heapq.heappop(pq)) # 사용법이 익숙치 않기 때문에 익숙해 지도록 하자.



# 맵
m = {}
m["first"] = 1
m["second"] = 2
for k in m :
    print(k, m[k])


# 집합
s = set()
s.add(123)
s.add(123)
s.add(456)
s.remove(123)

for i in s:
    print(i)
