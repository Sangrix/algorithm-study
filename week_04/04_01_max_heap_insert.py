#    0   1  2  3  4  5  6
# [None, 8, 6, 3, 4, 2, 5] -> 완전 이진트리를 배열로 편하게 표현하려고 None

# 왼쪽의 자식 노드는 부모 노드 index * 2, 오른쪽 자식 노드는 부모 노드 index*2 +1

#        3     level 0
# -> [None, 3]

# 1. 맨 뒤에 원소를 넣는다.
# 2. 부모와 비교해서 자기가 높으면 바꾼다
# 3. 2의 과정을 부모가 더 크거나 루트 노드에 도달했을 때까지 반복한다

# 1. 맨 뒤에 넣는다
#       3     level 0
#     4       level 1
# 자식의 index를 나누기 2하고 내림하면 부모 인덱스
# -> [None, 3, 4]

# 2. 부모와 비교한다
#       3     level 0
#     4       level 1

# 2. 자리를 바꾼다
#       4     level 0
#     3       level 1
# -> [None, 4, 3]

# 3. 반복을 끝낸다
#       4     level 0
#     3       level 1
# -> [None, 4, 3]

#       4     level 0
#     3   2   level 1
# -> [None, 4, 3, 2]

#       4     level 0
#     3   2   level 1
#   9         level 2
# -> [None, 9, 4, 3, 2]

#======================================================#
class MaxHeap:
  def __init__(self):
    self.items = [None]

  def insert(self, value):
    # 1. 원소를 맨 끝에 추가한다
    self.items.append(value)

    cur_index = len(self.items) - 1  # 가장 마지막 위치 인덱스

    # 2. 원소의 인덱스가 루트 노드(인덱스가 1)일 때까지 반복
    #           cur
    #  0     1  2
    # [None, 4, 9]

    #       cur
    #  0     1  2
    # [None, 4, 9]

    while cur_index != 1: # 1인 경우에는 root node라서 더 비교할 게 없음
      # 3. 부모 노드랑 비교해서 내가 더 크면 위치를 바꾼다
      parent_index = cur_index // 2

      if self.items[cur_index] > self.items[parent_index]:
        self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
        cur_index = parent_index
      else:
        break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!