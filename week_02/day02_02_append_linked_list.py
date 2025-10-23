# 노드는 화물 1칸으로 기억하면 됨

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

node = Node(5)
print(node.data, node.next)

# 맨 앞 칸만 LinkedList에 저장해 두는 것

class LinkedList:
  def __init__(self, value):
    self.head = Node(value)

  # LinkedList의 가장 끝에 있는 노드에 새로운 노드를 연결해줘
  def append(self, value):
    cur = self.head

    while cur.next is not None:
      cur = cur.next

    cur.next = Node(value)

  # LinkedList에서 지정한 head를 따라가면서 현재 있는 노드들을 전부 출력해주는 함수
  def print_all(self):
    cur = self.head

    while cur is not None:
      print(cur.data)
      cur = cur.next

  def get_node(self,index):
    cur = self.head
    cur_index = 0

    while cur_index != index:
      cur = cur.next
      cur_index += 1

    return cur

linked_List = LinkedList(5)
print(linked_List.head.data)

linked_List.append(12)
linked_List.append(8)

print(linked_List.get_node(1).data)

linked_List.print_all()

# [5] -> [3] -> [7] head 뒤가 아니라, head에서 연결되어 있는 노드들을 타고 지나가서
# 맨 마지막에 있는 노드에다가 뒤에 붙여달라는 뜻
# head에서 맨 뒤에 있는 것에 next에 넣어달라
# cur를 하나 지정해서 head = cur 이후 cur에 계속 next를 박아 주면 됨

# LinkedList 관련 문제에서는 항상 head에서 어떻게 이동하지? 를 먼저 고민해야함
# 그것을 하기 가장 좋은 방법은 cur를 고민하는 것