# 0123
# (())

# 인덱스 0 -> 열림
# stack = ["("]
# 인덱스 1 -> 열림
# stack = ["(", "("]
# 인덱스 2 -> 닫힘 (1번째)
# 제거해줘라
# 인덱스 3 -> 닫힘 (0번째)
# 제거해줘라

# -> 닫는 괄호가 나오면, 바로 직전에 열렸던 괄호가 닫힌다
# 열린 괄호가 나오면 순서대로 쌓아서 저장해야되는구나 -> Stack

# ["(" , "("]로 그냥 쌓아두고, 닫힘 나오면 pop()

# 닫힌 괄호가 나왔는데 스택이 비어? 올바르지 못한 문장이라는 것

def is_correct_parenthesis(string):
  stack = []
  for i in range(len(string)):
    if string[i] == "(":
      stack.append("(")

    elif string[i] == ")":
      if len(stack) == 0:
        return False

      stack.pop()

  if len(stack) != 0:
    return False
  else:
    return True

# =============================================================================#
# 1. 입력 순서 점검 ... 재귀?
# 2. 개수 동일 여부 확인

def is_my_correct_parenthesis(string):
  count_left = 0
  count_right = 0

  for i in range(len(string)):
    if string[i] == "(":
      count_left += 1
    else:
      count_right += 1

  return count_left == count_right


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
