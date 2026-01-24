shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_my_available_to_order(menus, orders):
  true_arr = [False,False,False]
  idx = 0

  for elem_order in orders:
    for elem_menu in menus:
      if elem_menu == elem_order:
          true_arr[idx] = True
    idx += 1

  for elem in true_arr:
    if elem == False:
      return False

  return True

result_1 = is_my_available_to_order(shop_menus, shop_orders)
print(result_1)

#=======================================================================#
# 오더에 있는 값이 메뉴에 존재하는 지 확인
# 특정 원소가 배열에 포함 되어있는 지 여부를 찾는데 이진 탐색이 가장 효율적
# 존재하는지 여부를 볼 때 set 자료형도 쓰인다

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # O(NlogN) + O(M) * O(logN) = O((N+M)*log(N))
    menus.sort() # 정렬: 메뉴의 길이 N -> O(NlogN)
    for order in orders: # 오더의 길이가 M이면 O(M)
      if not is_exist_target_number_binary(order, menus): # O(logN)
        return False

    return True

def is_exist_target_number_binary(target, array):
  current_min = 0
  current_max = len(array) - 1
  current_guess = (current_min + current_max) // 2

  while current_min <= current_max:
    if array[current_guess] == target:
      return True

    elif array[current_guess] < target:
      current_min = current_guess + 1

    else:  # array[current_guess] > target
      current_max = current_guess - 1

    current_guess = (current_min + current_max) // 2

  return False


result_2 = is_available_to_order(shop_menus, shop_orders)
print(result_2)

#===============================================================#
shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order_v1(menus, orders):
  # O(N) + O(M) * O(1) = O(N+M)
  menus_set = set(menus) # O(N)
  for order in orders: # M -> O(M)
    if order not in menus_set: # O(1)
      return False
  return True

result_3 = is_available_to_order_v1(shop_menus, shop_orders)
print(result_3)