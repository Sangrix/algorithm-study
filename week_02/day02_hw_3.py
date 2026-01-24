# 좀 더 쉬운 예제로 생각해보자
# [2,3,1] 과 0

# 모든 경우의 수를 다 해봐야지만 풀 수 있는 문제
# 1. +2+3+1 = 6
# 2. +2+3-1 = 4
# 3. +2-3+1 = 0 !!
# 4. +2-3-1 = -2
# 5. -2+3+1 = 2
# 6. -2+3-1 = 0 !!
# 7. -2-3+1 = -4
# 8. -2-3-1 = -6

# 좀 더 단순화하면(약간 가족 구성도처럼 분화해서 내려감)
# 1. +2 +3 -> +1 또는 -1
# 2. +2 -3 -> +1 또는 -1
# 3. -2 +3 -> +1 또는 -1
# 4. -2 -3 -> +1 또는 -1

# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는 N-1의 길이의 배열에서 마지막 원소를 뺀 경우의 수를 추가하면 된다
# [2,3]을 배치하는 경우에서, 맨 마지막 원소인 1을 더하냐 빼냐에 따라 경우의 수를 구할 수 있다

# 반복되는 구조를 재귀함수를 통해서 해결할 수 있다

numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
  all_ways=[]
  target_count = 0

  def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
    if current_index == len(array):
      all_ways.append(current_sum)
      return
    print(current_index, current_sum)
    get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
    get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

  # 초기 호출
  get_all_ways_by_doing_plus_or_minus(array,0,0)
  print("all_ways is ", all_ways)

  for way in all_ways:
    if target == way:
      target_count += 1
  return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!

