print("sort():리스트의 순서를 알파벳 순서로 영구히 변경")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

print("\n알파벳 순서의 역순으로 영구히 변경")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


print("\nsorted():리스트의 원래 순서를 유지하면서 임시로 정렬")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)


print("\nreverse():리스트의 원래 순서를 거꾸로")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print("\nlen():리스트의 길이를 반환")
# 리스트의 길이는 인덱스와 달리 1에서 시작함
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))