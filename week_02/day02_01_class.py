# self는 자기 자신을 가져오기 위한 정보일 뿐, 파라미터로 전달하지 않아도 됨

class Person:

  def __init__(self, name_param):
    self.name = name_param
    print("hihi i am created", self)

  def talk(self):
    print("hi i'm", self.name)


person_1 = Person("유재석")
print(person_1)
print(person_1.name)
person_1.talk()

person_2 = Person("박명수")
print(person_2)
print(person_2.name)
person_2.talk()