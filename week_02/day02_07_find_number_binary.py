finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# 정렬 되어있지 않은 배열에서는 이진 탐색을 사용할 수 없음

def is_exist_target_number_binary(target, array):
  current_min = 0
  current_max = len(array) - 1
  current_guess = (current_min + current_max) // 2
  find_count_bi = 0

  while current_min <= current_max:
    find_count_bi += 1
    if array[current_guess] == target:
      print(find_count_bi)
      return True

    elif array[current_guess] < target:
      current_min = current_guess + 1

    else:  # array[current_guess] > target
      current_max = current_guess - 1

    current_guess = (current_min + current_max) // 2

  return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)