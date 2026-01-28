# 인덱스의 관점에서 비교
# 구체한 상수값으로 구현을 해보고, 치환해주는게 구현 이해에 좋음

# i=0, j = i+1
#   v v v v
# 0 1 2 3 4

#     v v v
# 0 1 2 3 4

#       v v
# 0 1 2 3 4

#         v
# 0 1 2 3 4

# 인덱스 출력
# 1,2,3,4 -> 2,3,4 -> 3,4 -> 4

#  0  1  2  3
# [1, 2, 3, 2,3]

# for i in range(0, 4, 1): # 비교 대상
#   for j in range(i+1, 5, 1): # 비교 할 것

# i j
# 0 1~4
# [1, 2, 3, 2, 3]

# =================================================#
prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
  result = [0] * len(prices)

  for i in range(0, len(prices)-1, 1):
    price_not_fall_period = 0
    for j in range(i + 1, len(prices), 1):
      if prices[i] <= prices[j]:
        price_not_fall_period += 1
      else:
        price_not_fall_period += 1
        break

    result[i] = price_not_fall_period

  return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))
