# 반복되지 않는 첫번째 알파벳
# 반복되는지 아닌지를 판단
# string에서 알파벳의 빈도수를 찾는다.
# 그리고 빈도수가 1인 알파벳들 중에서 string에서 뭐가 먼저 나왔는지를 찾아본다.

input = "abadabac"

def find_not_repeating_first_character(string):
    occurrence_array = find_max_occurred_alphabet(string)

    not_repeating_character_array = []
    for index in range(len(occurrence_array)):
      alphabet_occurrence = occurrence_array[index]
      if alphabet_occurrence == 1:
        not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
      if char in not_repeating_character_array:
        return char

    return "_"


def find_max_occurred_alphabet(string):
  count_array = [0] * 26

  for elem in string:
    if not elem.isalpha():  # 알파벳 여부 검사
      continue
    arr_index = ord(elem) - ord('a')  # 해당 문자를 인덱스로 치환
    count_array[arr_index] += 1  # count 배열에 인덱스로 찾아가서 해당 값을 +1

  return count_array

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))