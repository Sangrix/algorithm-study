# 1. 이중 반복문 -> O(N^2)
# for student in all_students: O(N)
#   is_present = False
#   for present_student in present_students: -> O(N)
#     if student == present_student:
#       is_present = True
#   if not is_present:
#     return student

# 2. 정렬 O(NlongN + N) -> O(NlogN)
# 정렬 이후 O(NlogN)
# 하나하나 원소들을 보면서 O(N) 존재하지 않는 학생을 찾으면 결석을 찾을 수 있음

# 3. Dictonary, Hash table O(N)
# O(N), 학생등록 최선 1, 최악 N이지만  알고리즘 풀 때는 최선으로 고려
# 제거의 경우도 최선은 1, 최악은 N이지만  알고리즘 풀 때는 최선으로 고려
# all_students들을 돌면서, hast table의 키값에 해당하는 학생들을 등록
# present_students를 돌면서 hase table의 키값의 값을 제거한다
# 그러고 남아있는 hash table의 키 값에 해당하는 학생이 결석한 학생


#========================================================================================#
all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

def get_absent_student(all_array, present_array):
    dict = {}
    for student in all_array:
      dict[student] = True # 키 값이 딕셔너리에 존재하는지만 보면 됨

    for present_student in present_array:
      del dict[present_student] # 딕셔너리에 대한 키 값을 제거하는 방법 -> del 딕셔너리명[key]

    print("hihi", dict.keys()) # 딕셔너리의 키값을 반환

    for key in dict.keys():
      return key # 반드시 한 명이라 바로 반환, 여러명이면 dict의 키 값을 모두 반환해줘야함


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))