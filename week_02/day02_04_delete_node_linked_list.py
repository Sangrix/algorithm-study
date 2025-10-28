# LinkedList 관련 문제에서는 항상 head에서 어떻게 이동하지? 를 먼저 고민해야함
# 그것을 하기 가장 좋은 방법은 cur를 고민하는 것
# 핵심은 head와 current node이다!!

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

# ["자갈"] -> ["밀가루"] -> ["우편"]
# ["흑연"]을 자갈 뒤에 넣고 싶다면
# 1) ["자갈"] -> ["흑연"]을 연결하고
# 2) 흑연 칸의 다음 칸을 밀가루로 연결해주면 된다.

# 그러려면 일단 새로운 노드를 하나 만들고 붙여줘야함
# index -1번째의 노드가 필요하다.

# 일단 우리는 head 노드만 저장하기 때문에 기존 index 자리의 노드를 저장이 선행되어야 함
# 저장하지 않으면 찾을 방법이 없다

# -1이 입력되면 0일 때는 어떻게 될 지 항상 고려해야함

  def add_node(self, index, value):
    new_node = Node(value)

    if index == 0:
      new_node.next = self.head
      self.head = new_node
      return

    prev_node = self.get_node(index - 1)

    next_node = prev_node.next
    prev_node.next = new_node
    new_node.next = next_node

# index - 1 번째 칸에서 index + 1번째 칸으로 연결 되도록 하면 됨
# -1 은 동일하게 0번째를 신경써줘야 함
  def delete_node(self, index):
    if index == 0:
      self.head = self.head.next
      return

    prev_node = self.get_node(index - 1)
    index_node = self.get_node(index)
    # prev idx next
    # [7]->[5]->[6]->[12]->8
    prev_node.next = index_node.next



linked_List = LinkedList(5)
print(linked_List.head.data)

linked_List.append(12)
linked_List.append(8)

print(linked_List.get_node(1).data)

linked_List.print_all()

linked_List.add_node(1,6)
linked_List.print_all()

linked_List.add_node(0,7)
linked_List.print_all()

linked_List.delete_node(0)
linked_List.print_all()

# [5] -> [3] -> [7] head 뒤가 아니라, head에서 연결되어 있는 노드들을 타고 지나가서
# 맨 마지막에 있는 노드에다가 뒤에 붙여달라는 뜻
# head에서 맨 뒤에 있는 것에 next에 넣어달라
# cur를 하나 지정해서 head = cur 이후 cur에 계속 next를 박아 주면 됨