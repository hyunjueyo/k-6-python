motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

print("요소 바꾸기")
motorcycles[0]='ducati'
print(motorcycles)

print("append() : 리스트 마지막에 요소 추가")
motorcycles.append('GM')
print(motorcycles)

print("insert(1,'') : 원하는 위치에 요소 삽입")
motorcycles.insert(1,'Samcheonri')
print(motorcycles)

print("del : 요소 삭제하기")
del motorcycles[0]
print(motorcycles)