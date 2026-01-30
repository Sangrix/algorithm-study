# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 장르끼리 묶어서 총 재생횟수 구하고, 가장 많은 장르부터 2곡을 넣어줌
# -> genre_array에서 genre 별로 재생횟수를 모두 모아서 비교해준다. 그리고 가장 많이 재생된 장르 별로 노래를 2곡씩 넣는다

# 특정 키 값은 아직 정해지지 않았다
# 특정 키 값에 대해서 value를 모아서 합쳐주고 싶다
# dict = {}
# dict = {"pop" : 0, "classic": 0}

#      0        1        2          3         4
# ["classic", "pop", "classic", "classic", "pop"]
# [500, 600, 150, 800, 2500]

# 0.
# -> dict = {"classic" : 500}
# -> dict2 = {"classic" : [(0, 500)]}

# 1.
# -> dict = {"classic" : 500, "pop" : 600}
# -> dict2 = {"classic" : [(0, 500)], "pop" : [1, 600]}

# 2.
# -> dict = {"classic" : 500 + 150, "pop" : 600}
# -> dict2 = {"classic" : [(2, 150)], "pop" : [1, 600]}


# 가장 많이 재생된 장르들을 순서대로 알려주세요 -> value 기준으로 정렬


# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# -> 많이 재생된 장르 별로 2곡을 넣어줄때, 많이 재생된 노래 먼저 넣어줘야 한다
# 이번 딕셔너리는 어떤 인덱스에 어떤 플레이 횟수를 가지고 있는지에 대한 저장


# 3. 장르 내에서 재생횟수가 같다면, 고유번호(인덱스)가 낮은 노래 먼저 수록

# "많이" "가장 많이" 같은 개념이 나오면 -> "정렬을 써야 하는구나."

#============================================================#
def get_melon_best_album(genre_array, play_array):
  # 1. dict에 장르별로 얼마나 재생횟수를 가지고 있는지
  # 2. dict에 장르별로 어느 인덱스에 몇번 재생횟수를 가지고 있는지

  n = len(genre_array)
  genre_total_play_dict = {}
  genre_index_play_array_dict = {} # {"classic" : [(index, play), (), ()]}

  for i in range(n):
    genre = genre_array[i] # classic
    play = play_array[i] # 500

    if genre in genre_total_play_dict: # classic이라는 키값이 있었으면
      genre_total_play_dict[genre] += play # 재생횟수를 더해줘
      genre_index_play_array_dict[genre].append([i, play])
    else:
      genre_total_play_dict[genre] = play # 500
      genre_index_play_array_dict[genre] = [[i, play]]

  # 장르별로 가장 재생횟수가 많은 장르들중, 곡수가 많은 순서대로 2개씩 출력하기
  # 배열에다 키 값과 vlaue 값이 개별적으로 들어간 자료구조

  # items -> 딕셔너리에 들어있는 data를 하나씩 꺼내고 싶을 때 사용합니다.
  # 딕셔너리가 가진 키(Key)와 값(Value)의 쌍을 튜플(Tuple) 묶음으로 반환해주는 아주 유용한 함수

  # .items() 호출 결과 (실제로는 dict_items라는 특수 객체 반환)
  # user_scores = {"Alice": 90, "Bob": 85, "Charlie": 95}
  # [('Alice', 90), ('Bob', 85), ('Charlie', 95)] 와 유사한 형태
  # genre_total_play_dict.items()

  # sorted 함수 -> 특정 배열 값을 입력받아서 정렬해줄 수 있게 만드는 함수
  # ()로 감싸진 자료구조는 tuple
  # 람다 함수 key = lambda item: item[1], 튜플 내에 있는 1번째 원소를 기준으로 정렬
  sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item:item[1], reverse = True)

  result = []
  # 튜플을 반복문에서 사용하려면, 형태 개수 대로 변수가 있어야 함
  for genre, total_play in sorted_genre_play_array:
    sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item:item[1], reverse=True)

    # play 순서로 정렬된 것들의 인덱스를 반환해줘야함
    # 장르별로 높은 2개 넣기
    genre_song_count = 0
    for index, play in sorted_genre_index_play_array:
      if genre_song_count >= 2:
        break

      result.append(index)
      genre_song_count += 1

  return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ",
      get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ",
      get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"],
                           [2000, 500, 600, 150, 800, 2500, 2000]))