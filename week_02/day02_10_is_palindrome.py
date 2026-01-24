# 눈이 하는 행동을 풀어서 써보는 게 좋음

# v   v
#  v v
# abcba

input = "abcba"

def is_palindrome(string):
  n = len(string)

  for i in range(n): # 0 ~ n-1
    if string[i] != string[n- 1 - i]:
      return False

    return True

print(is_palindrome(input))

#===========================================#
# 문자열의 탐색 범위를 줄여가면서 찾을 수 있음
# 맨 앞과 맨 뒤가 같으면 잘라내고 남은 부분으로 탐색
# 0 ~ n-1
# 1 ~ n-2

def is_palindrome_recursive(string):
  if string[0] != string[-1]:
    return False
  if len(string)<=1:
    return True

  return is_palindrome_recursive(string[1:-1])

print(is_palindrome_recursive(input))