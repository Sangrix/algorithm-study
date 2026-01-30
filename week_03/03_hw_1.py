# 최대한 할인을 많이 받는다? -> 가장 비싼 금액이 가장 높은 할인을 받는다
# 정렬된 데이터가 필요하겠구나 -> sort()
# 내림차순을 위해서는 .sort(reverse=True)
# 개수가 다를 수 있기 때문에 while을 사용할 것

def get_max_discounted_price(prices, coupons):
  prices.sort(reverse=True)
  coupons.sort(reverse=True)

  price_index = 0
  coupon_index = 0
  max_discounted_price = 0

  while price_index < len(prices) and coupon_index < len(coupons):  # 가격과 쿠폰이 모두 배열 내 원소일 때
    discount_price = prices[price_index] * (100 - coupons[coupon_index]) / 100
    max_discounted_price += discount_price

    price_index += 1
    coupon_index += 1

  while price_index < len(prices): # 즉, 현재 price_index가 prices 길이 범위 내라면, 나머지 원가 추가
    max_discounted_price += prices[price_index]
    price_index += 1

  return max_discounted_price

#==========================================================================#
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def my_get_max_discounted_price(prices, coupons):
  prices.sort()
  coupons.sort()
  result_price = 0

  while prices and coupons:
    result_price += (prices.pop()) * ((100 - coupons.pop()) * 0.01)

  while prices:
    result_price += prices.pop()

  return int(result_price)


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))
