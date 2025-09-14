# for else?? for문이 끝났을 때, else문에서 출력 -> 다만 for문 안에서 중단되면 else가 출력 x
# 특정 반복문이 있을 때, break하지 않고 모두 돌았는지 확인하기 위함, break되면 else 실행 x

for x in ["맨유", "맨유", "아스날", "맨유"]:
  if x != "맨유":
    break
else:
  print("모두 맨유 팬이시군요. 제가 맥주를 쏘겠습니다.")


# 내 생각: 0 ~ input까지 반복문을 돌리며 1과 자기 자신으로만 나뉘면 기록
# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
# 소수 리스트를 반환해야 한다.
# 2~input까지 찾아서 이것들이 소수라면 prime_list에 넣어라!

# 개선1) 사실 소수들과 input을 비교하면 됨. 2로 안 나눠 떨어지는데 6으로 나눠 떨어지지 않기 때문.
# -> for i in range(2, n)을 for i in prime_list로 돌리면 됨

# 개선2) 소수 -> n의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
# -> i * i <= n 일 때까지

# 모두 알 필요는 없다. -> 모든 알고리즘은 개선 가능하다는 태도만 가지고 가면 된다.

input = 20

def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number+1):
      for i in range(2, n): # 2부터 n-1까지를 반복
        if n % i == 0:
          break
      else:
        prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)