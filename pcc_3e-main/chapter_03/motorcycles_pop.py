# pop() : 리스트의 마지막 요소를 제거하는 동시에 해당 요소를 반환
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# pop()메서드 활용
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# 임의의 위치에서 요소 꺼내기
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# 리스트에서 요소를 제거하고 그 요소를 쓸 일이 더는 없다면 del문
# 제거한 요소를 사용할 생각이라면 pop() 메서드 사용