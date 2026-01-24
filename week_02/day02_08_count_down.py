def count_down(number):
  if number < 0:
    return

  print(number)  # number를 출력하고
  count_down(number - 1)  # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)
# print(60) -> count_down(59)
# print(59) -> count_down(58)
# print(0) -> count_down(-1)
# ... 무한 호출로 인해 운영체제가 kill -> max_recursion_exceed

# 탈출 조건을 줘서 return을 통해 재귀 함수 탈출 조건 고려