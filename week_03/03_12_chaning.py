# dict = {"fast": "빠른"}
# put(key, value) -> dictonary에 key에 해당하는 곳에 value를 저장해두겠다
# get(key) -> dictonary에 key에 해당하는 value를 반환해라


# a b c d e ... z 26개인데
# [0, 1, ... ,8] 8개임
# 1. Chaning 기법 : 충돌이 발생했을 때, 그 값들을 링크드 리스트로 관리

class LinkedTuple:
  def __init__(self):
    self.items = []

  def add(self, key, value):
    self.items.append((key, value))

  def get(self, key):
    for k, v in self.items:
      if k == key:
        return v

linked_tuple = LinkedTuple()

linked_tuple.add("333", 7)
linked_tuple.add("77", 6)
print(linked_tuple.items)

print(linked_tuple.get("333"))


class LinkedDict:
  def __init__(self):
    self.items = []
    for i in range(8):
      self.items.append(LinkedTuple)

  def put(self, key, value):
    index = hash(key) % len(self.items)

    self.items[index].add(key, value) # index번째의 LinkedTuple에 [(key, value)]
                                      # 한 번 더 호출되면? [(key, value), (key2, value2)]

  def get(self, key):
    index = hash(key) % len(self.items)
    return self.items[index].get(key) # LinkedTuple에 [(key, value), (key2, value2)]

# my_dict = Dict()
#
# my_dict.put("test", 3)
# my_dict.put("333", 7)
# my_dict.put("77", 6)

# self.itmes[1] = [7] -> [6]의 링크드 리스트 형태
# 하지만 key의 hash 값만 가지고는 링크드리스트에서 위치를 알 수 없음
# key-value를 같이 저장하도록 해야함
# self.items[1] = ["333", 7] -> ["77", 6]

# print(my_dict.get("333"))
# 1. 333을 hash해서 나머지 값 -> 즉, 인덱스를 구함 -> 1
# 2. self.items[1] -> ["333", 7] -> ["77", 6]
# 3. ["333", 7] 에 있네 그러면 value는 7이야