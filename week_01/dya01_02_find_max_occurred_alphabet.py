# ascii code
# 컴퓨터를 통해서 문자를 저장하고 싶은데, 컴퓨터는 숫자밖에 저장할 수 없으니
# 문자를 나타내기로 약속한 숫자들을 정해놓고, 그 숫자를 바로 ASCII 코드라고 한다.


# 이게 알파벳인지 알고 싶다.
# isalhpa() 함수를 활용


# a~z
# [0] -> a, [1] -> b, [25] -> z
# ord()함수를 활용
print(ord('a'))
print(ord('a') - 97)


# 1번째 인덱스에 무슨 알파벳을 넣은건지 알고 싶다.
# chr() 함수를 활용
print(chr(97))


# 1. a,b,c처럼 문자가 해당 문자열에 얼마나 있는지 확인하고, 그 개수가 가장 크다면 반환해줘야하는 값을 알파벳으로 변환.
# a -> 0 max_occurence = 0, max_alphabet = a

# 2. [0] * 26 각 알파벳의 빈도수를 저장한 배열을 만든다.
# 그리고 string을 돌면서 해당 문자가 알파벳이라면, 알파벳을 인덱스화 시켜서 알파벳의 빈도수를 업데이트 한다.
# a -> 0번째 인덱스 값을 +1, z -> 25번째 인덱스 값을 +1


def find_max_occurred_alphabet(string):
    count_array = [0] * 26

    for elem in string:
        if not elem.isalpha():  # 알파벳 여부 검사
            continue
        arr_index = ord(elem) - ord('a')  # 해당 문자를 인덱스로 치환
        count_array[arr_index] += 1  # count 배열에 인덱스로 찾아가서 해당 값을 +1

    max_count = 0
    max_alphabet_index = 0

    for index in range(len(count_array)):
        if count_array[index] > max_count:
            max_count = count_array[index]
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))

print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))


