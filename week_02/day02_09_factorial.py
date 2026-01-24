# 수학 문제가 나오면 수학적 수식을 최대한 써보는 것
# factorial(n) = n * factorial(n-1)
# factorial(n-1) = (n-1) * factorial(n-2)

# factorial(1) = 1

def factorial (n):
  if n <= 1:
    return 1

  return n * factorial(n - 1)

print(factorial(5))