# 레이저를 왼쪽으로 쏘니까, 왼쪽에 있는 것들 중 먼저 맞는 걸 찾아줘야겠구나

# 오른쪽으로 넣는 스택으로 생각
# 오른쪽부터 하나씩 pop되는 형태

#=======================================================#
top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
  answer = [0] * len(heights) # [0, 0, 0, 0, 0]

  while heights: # is_empty와 동일한 효과, 비어있지 않으면 True
    height = heights.pop() # 4
    # 레이저를 왼쪽으로 쏘니까 3,2,1,0으로 인덱스
    # heights = [6,9,5,7]

    for i in range(len(heights)-1,-1,-1):
      if height <= heights[i]:
        answer[len(heights)] = i+1
        break

  return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))