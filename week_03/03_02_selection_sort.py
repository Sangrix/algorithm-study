# 1.
# i = 0, j는 5개 보기
#  0 1 2 3 4
# [4,6,2,9,1]

# 2.
# i = 1, j는 4개 보기
#    0 1 2 3
# [4,6,2,9,1]

# 3.
# i = 2, j는 3개 보기
#      0 1 2
# [4,6,2,9,1]

# 4.
# i = 3, j는 2개 보기
#        0 1
# [4,6,2,9,1]


# for i in range(5-1):
#   for j in range(5-i):
#     print(i+j)


# i가 0일때 전체에서 가장 작은 걸 뽑아야 함
# ======================================================= #
input = [4, 6, 2, 9, 1]

def selection_sort(array): # O(n^2)
    n = len(array)
    for i in range(n-1): # O(n)
      min_index = i # i = 0

      for j in range(n-i): # j = 0 ~ 4 , O(n)
        if array[i+j] < array[min_index]:
          min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]

    return array

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))