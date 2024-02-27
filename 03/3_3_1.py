cars = ['bmw', 'audi', 'toyota', 'sabaru']
# sort() : 리스트 순서를 영구히 정렬
cars.sort(reverse=True)
print(cars)
# 정렬 안된 거 확인
print(sorted(cars))
print(cars)

print(sorted(cars,reverse=True))
print(cars)

# len() : 리스트의 길이를 반환
print(len(cars))
# print(cars[4]) 3까지만 있으니까 오류뜸, 안전하게 print(cars[-1])로 하는 게 좋다
