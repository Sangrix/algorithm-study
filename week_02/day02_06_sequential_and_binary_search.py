finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    find_count_seq = 0
    for number in array:
        find_count_seq += 1
        if target == number:
            print(find_count_seq)
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# ========================================================================================= #
# N
# 1~N
# 처음: 1...N
# 1번 탐색: 1...N/2
# 2번 탐색: 1...N/4
# k번 탐색: 1...N/2^k
#
# N/2^k -> 1이 되려면
# N = 2^k
# log_2(N) = k -> k번 탐색을 하면 1개의 원소를 찾을 수 있다.
#
# 시간복잡도
# O(log(N)) : 대강 연산량이 반으로 나눠지는구나 싶으면 log(N)임

def is_existing_target_number_binary(target, array):
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

        else: #array[current_guess] > target
            current_max = current_guess - 1

        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)