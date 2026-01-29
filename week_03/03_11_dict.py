# dict = {"fast": "빠른"}
# put(key, value) -> dictonary에 key에 해당하는 곳에 value를 저장해두겠다
# get(key) -> dictonary에 key에 해당하는 value를 반환해라

class Dict:
  def __init__(self):
    self.items = [None] * 8

# a b c d e ... z 26개인데
# [0, 1, ... ,8] 8개임
# 1. Chaning 기법 : 충돌이 발생했을 때, 그 값들을 링크드 리스트로 관리

  def put(self, key, value):
    index = hash(key) % len(self.items)
    self.items[index] = value

  def get(self, key):
    index = hash(key) % len(self.items)

    return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
my_dict.put("333", 7)
# self.items[1] = 7
my_dict.put("77", 6)
# self.items[1] = 6
# self.itmes[1] = [7] -> [6]의 링크드 리스트 형태

# 인덱스로 매핑되어 데이터를 덮어 씌움 -> collision

print(my_dict.get("test"))