### 배열
삽입/삭제 : O(N)
탐색 : O(1)
python에서는 list를 사용
삽입/삭제 시에는 리스트 전체를 탐색하고 삽입, 삭제 할 자리를 찾기 때문에 O(N) 
탐색 시에는 인덱스 번호와 자료형의 바이트 수를 안다면 리스트의 시작 주소에서 이 값을 더할 경우 한번에 접근 가능 이를 random access 라고 칭함


### 벡터
삽입/삭제 : O(N)
탐색 : O(1)
보통 2개의 값을 쌍으로 저장할 때 사용
쌍으로 값을 저장하면 10개의 값을 저장하더라도 자료형의 길이는 5가 나오게 됨


### 스택
삽입/삭제 : O(1)
FILO


### 큐
삽입/삭제 : O(1)
FIFO


### 우선순위 큐
삽입/삭제 : O(logN)
이진트리 형태를 가지며 python의 경우 가장 작은 값이 root가 되는 min-heap 형태


### 맵
삽입/삭제 : O(1)
key, value 형태를 가지며 python에서는 dictionary라고 함
python의 경우 삽입/삭제 시 O(1)이 나오는 이유는 key값이 hash 함수를 통해 value를 얻을 수 있기 때문



### 집합
삽입/삭제 : O(1)
중복을 허용하지 않음