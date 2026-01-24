class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self, value):
    self.head = Node(value)

  def append(self, value):
    cur = self.head
    while cur.next is not None:
      cur = cur.next
    cur.next = Node(value)

  def my_get_kth_node_from_last(self, k):
    idx = 0
    cur = self.head
    while cur.next is not None:
      cur = cur.next
      idx += 1

    cur = self.head

    for _ in range(idx-(k-1)):
      cur = cur.next

    return cur

#====================================================#
  def get_kth_node_from_last_v1(self, k):
    length = 1
    cur = self.head

    while cur.next is not None:
      cur = cur.next
      length += 1

    print("length is = ", length)
    end_length = length - k
    cur = self.head

    for i in range(end_length):
      cur = cur.next

    return cur

#===================================================#
  def get_kth_node_from_last_v2(self, k):
    slow = self.head
    fast = self.head

    for i in range(k):
      fast = fast.next

    while fast is not None:
      slow = slow.next
      fast = fast.next

    return slow

#==============================================================================#
# head
#        cur
# 맨 끝에 도달하고 왼쪽으로 1칸

# 그냥 링크드리스트를 다루는 방법에 이러한 로직도 있구나 정도로 알아두면 됨
# 1. 어디가 끝인지 알아내는 방법

# 2. 먼저 k개 전에 있는 노드를 가리키는 포인터를 추가 생성해서 같이 이동
# slow        fast
#       slow         fast

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.my_get_kth_node_from_last(2).data) # 7이 나와야 합니다!
print(linked_list.get_kth_node_from_last_v1(2).data)