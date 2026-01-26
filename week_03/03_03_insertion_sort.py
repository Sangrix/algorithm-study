# 삽입 정렬은 가장 앞에 있는 것을 기준으로 이미 정렬된 상태로 보는 것

# 새로운 부대원을 넣을 때부터 비교하는 컨셉
# 0번째는 이미 정렬된 상태라 1번째 인덱스부터 값 비교
#     1
# [4, 6, 2, 9, 1]

#     1  2
# [4, 6, 2, 9, 1]

# 1 -> 1,2 -> 1,2,3 -> 1,2,3,4

# i = 1, j = 0 1
# i = 2, j = 0 2
# i = 2, j = 1 1
# for i in range(1,5):
#   for j in range(i):
#     print(i - j)

#======================================================#
input = [4, 6, 2, 9, 1]

# 모든 값을 사용하는 게 아니라, 앞은 다 정렬된 걸로 가정해서 비교 중간에 멈춰도 되는 정렬
def insertion_sort(array): # O(N^2), 오메가(N)
    n = len(array)
    for i in range(1, n): # O(N)
      for j in range(i): # O(N)
        if array[i-j] < array[i-j-1]:
          array[i - j], array[i - j - 1] = array[i-j-1],  array[i-j]
        else:
          break

    return array

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))