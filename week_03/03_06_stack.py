# 1. 한 곳에서만 자료를 빼고 넣는다
# 2. LIFO 구조
# 맨 위에 값만 알면 됨 -> 가장 마지막에 들어온 게 HEAD가 되도록 구현

# HEAD
# [4]

# HEAD
# [3] -> [4]


#========================================================#
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, value):
    new_head = Node(value) # [3]이라는 노드를 만듦
    new_head.next = self.head # [3] -> [4]
    self.head = new_head # [3] 이라는 노드를 head로 만들어줘

  # pop 기능 구현
  def pop(self):
    if self.is_empty():
      print ("Stack is empty")

    delete_head = self.head
    self.head = self.head.next # head = [3]

    return delete_head

  def peek(self):
    if self.is_empty():
      return "Stack is empty"

    return self.head.data

  # isEmpty 기능 구현
  def is_empty(self):

    return self.head is None

stack = Stack()

stack.push(4)
print(stack.peek())

stack.push(3)
print(stack.peek())

stack.push(5)
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())